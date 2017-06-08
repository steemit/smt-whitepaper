
OK, the whitepaper is complicated to build.  I'm sorry but that's the way it is.

- We want Google Docs for collaborative editing, commenting, and contribution by people who aren't familiar with Git.
- We want Markdown so we'll be able to copy-paste it into steemit.com, and so we can use LaTeX via Pandoc.
- We want the document to be version controlled so we can use Git to see history, do experiments in branches, etc.
- Images are created in Inkscape with SVG, but Google Docs doesn't allow SVG uploads (except via very convoluted workarounds).
- Actually Pandoc doesn't allow with PDF output either due to limitations in LaTeX [reference](https://github.com/jgm/pandoc/issues/265).

So what I've come up with is this:

- There is a version of the whitepaper in Google Docs.
- When editing the whitepaper in the master branch, edit it in Google Docs, then copy-paste it into your text editor and run the `fixws.py` script to import it into Git.
- When editing the whitepaper outside the master branch, upload it to a new Google Doc if you want to share it.
- If you want to merge changes to the whitepaper outside the master branch, manually edit the Google Doc to update it.
- DO NOT DO A FULL-DOCUMENT COPY-PASTE INTO THE GOOGLE DOC, I AM WORRIED THAT WILL RUIN IT (especially with comments).
- When finished updating the Google Doc, copy-paste from the Google Doc into the master branch to update the master branch.
- When doing this procedure, be sure to compare the resulting document (in master) to the original (in your branch) to make sure the merge was reasonable.
- If you want to see images in the Google Doc, you will have to manually convert them to PNG by installing Inkscape, running the `build-images.sh` script, and uploading the images manually.
- Don't forget to also check the images build in Markdown with `build-pdf.sh`.
