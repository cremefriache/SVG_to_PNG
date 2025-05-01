# SVG_to_PNG

Windows users:

• For this to work on Windows 64x, the Cairo library files need to be installed to PATH so Python/CairoSVG can find them. You can leverage MSYS2 to do this fairly easily.

Download the installer and follow the instructions -> https://www.msys2.org/

Install and update MSYS2 via the following:
```bash
pacman -Syu
```

```bash
pacman -Su
```

```bash
pacman -S mingw-w64-x86_64-cairo
```
If prompted, selected "Y".

Then, finally, for PATH

• Find your MSYS2 installation directory (usually C:\msys64).

• The path you need to add is typically C:\msys64\mingw64\bin (adjust drive/folder if you installed MSYS2 elsewhere).

• Search for "Edit the system environment variables" in the Windows Start menu.

• Click the "Environment Variables..." button.

• In the System variables section (or User variables if you only want it for your user), find the Path variable, select it, and click "Edit...".

• Click "New" and paste in the path (e.g., C:\msys64\mingw64\bin).

• Click OK on all the dialog windows.

• Restart your computer for good measure.
