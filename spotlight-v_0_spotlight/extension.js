const vscode = require('vscode');


const spotlightDecoration = vscode.window.createTextEditorDecorationType({
  opacity: '1.0',
  backgroundColor: 'rgba(255,255,255,0.02)'
});

const dimDecoration = vscode.window.createTextEditorDecorationType({
  opacity: '0.35'
});

let activeSpotlightTag = null;

function expandRangeToWholeLines(range, document) {
  const ranges = [];

  for (let line = range.start.line; line <= range.end.line; line++) {
    ranges.push(document.lineAt(line).range);
  }

  return ranges;
}


function applySpotlight(rangesByUri) {
  vscode.window.visibleTextEditors.forEach(editor => {
    const uriKey = editor.document.uri.toString();
    const spotlightRanges = rangesByUri.get(uriKey) || [];

    // Dim entire document
    const fullRange = new vscode.Range(
      editor.document.positionAt(0),
      editor.document.positionAt(editor.document.getText().length)
    );

    editor.setDecorations(dimDecoration, [fullRange]);
    editor.setDecorations(spotlightDecoration, spotlightRanges);
  });
}


function getCommentSyntax(document) {
  const lang = document.languageId;

  switch (lang) {
    case 'html':
      return {
        start: '<!-- ',
        end: ' -->'
      };

    case 'css':
      return {
        start: '/* ',
        end: ' */'
      };

    case 'javascript':
    case 'typescript':
    case 'java':
    case 'c':
    case 'cpp':
    case 'go':
    case 'rust':
      return {
        start: '// ',
        end: ''
      };

    case 'python':
    case 'shellscript':
      return {
        start: '# ',
        end: ''
      };

    default:
      return {
        start: '// ',
        end: ''
      };
  }
}




async function findTagRanges(tagName) {
	const files = await vscode.workspace.findFiles('**/*');

	const rangesByUri = new Map();

	for (const uri of files) {
		const doc = await vscode.workspace.openTextDocument(uri);
		const text = doc.getText();

		const startRegex = new RegExp(`#tag_${tagName}_start`, 'g');
		const endRegex = new RegExp(`#tag_${tagName}_end`, 'g');

		let startMatch;
		while ((startMatch = startRegex.exec(text))) {
			const endMatch = endRegex.exec(text);
			if (!endMatch) break;


			const startline = doc.positionAt(startMatch.index).line + 1;
			const endline = doc.positionAt(endMatch.index).line - 1;

			if (startline <= endline) {
				const startPos = new vscode.Position(startline, 0);
				const endPos = doc.lineAt(endline).range.end;

				if (!rangesByUri.has(uri.toString())) {
					rangesByUri.set(uri.toString(), []);
				}

				rangesByUri.get(uri.toString()).push(
					new vscode.Range(startPos, endPos)
				);
			}

		}
	}

	return rangesByUri;
}




async function collectTags() {
  const files = await vscode.workspace.findFiles('**/*');
  const tags = new Set();

  for (const uri of files) {
    const doc = await vscode.workspace.openTextDocument(uri);
    const matches = doc.getText().matchAll(/#tag_(\w+)_start/g);
    for (const m of matches) {
      tags.add(m[1]);
    }
  }

  return [...tags];
}

function activate(context) {

	context.subscriptions.push(
		vscode.commands.registerCommand(
			'spotlight.wrapSelectionWithTag',
			async () => {
				const editor = vscode.window.activeTextEditor;
				if (!editor) return;

				const document = editor.document;
				const selection = editor.selection;

				if (selection.isEmpty) {
					vscode.window.showInformationMessage(
						'Select a block of text to wrap with a tag.'
					);
					return;
				}

				const existingTags = await collectTags();

				const tagName = await vscode.window.showInputBox({
					prompt: 'Enter tag name',
					value: existingTags[0] || ''
				});

				if (!tagName) return;

				const comment = getCommentSyntax(document);

				const startLine = selection.start.line;
				const endLine = selection.end.line;

				const startPos = new vscode.Position(startLine, 0);
				const endLineText = document.lineAt(endLine);
				const endPos = endLineText.range.end;
				
				const indent = document.lineAt(startLine).firstNonWhitespaceCharacterIndex;
				const pad = ' '.repeat(indent);

				const startTag =
					`${pad}${comment.start}#tag_${tagName}_start${comment.end}\n`;

				const endTag =
					`\n${pad}${comment.start}#tag_${tagName}_end${comment.end}`;

				await editor.edit(editBuilder => {
					editBuilder.insert(startPos, startTag);
					editBuilder.insert(endPos, endTag);
				});

				// If this tag is currently spotlighted, refresh spotlight
				if (activeSpotlightTag === tagName) {
					const rangesByUri = await findTagRanges(tagName);
					applySpotlight(rangesByUri);
				}

			}
		)
	);



	context.subscriptions.push(
		vscode.commands.registerCommand('spotlight.selectTag', async () => {
			const tags = await collectTags();
			if (!tags.length) {
				vscode.window.showInformationMessage('No tags found.');
				return;
			}

			const selected = await vscode.window.showQuickPick(tags, {
				placeHolder: 'Select a spotlight tag'
			});

			if (!selected) return;

			activeSpotlightTag = selected;
			const rangesByUri = await findTagRanges(selected);
			applySpotlight(rangesByUri);
		}),



		vscode.commands.registerCommand('spotlight.clear', () => {
			vscode.window.visibleTextEditors.forEach(editor => {
				editor.setDecorations(dimDecoration, []);
				editor.setDecorations(spotlightDecoration, []);
			});

			activeSpotlightTag = null;
		})
	);
}

module.exports = { activate };
