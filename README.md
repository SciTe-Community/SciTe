# [SciTe](https://www.scintilla.org/SciTE.html)

Scintilla and Lexilla can be built by themselves.
To build SciTe, Scintilla and Lexilla should first be built.

See lexilla/README.md for information on building Lexilla.

### GTK+/Linux version

You must first have GTK+ 2.24 or later and GCC (7.1 or better) installed.
Clang may be used by adding CLANG=1 to the make command line.
Other C++ compilers may work but may require tweaking the make file.
Either GTK+ 2.x or 3.x may be used with 2.x the default and 3.x
chosen with the make argument GTK3=1.

To build Scintilla, use the makefile located in the scintilla/gtk directory
```sh
cd scintilla/gtk
make
cd ../..
```

To build and install SciTe, use the makefile located in the scite/gtk directory
```sh
cd scite/gtk
make
sudo make install
```

This installs SciTe into $prefix/bin. The value of $prefix is determined from
the location of Gnome if it is installed. This is usually /usr if installed
with Linux or /usr/local if built from source. If Gnome is not installed
/usr/bin is used as the prefix. The prefix can be overridden on the command
line like "make prefix=/opt" but the same value should be used for both make
and make install as this location is compiled into the executable. The global
properties file is installed at $prefix/share/scite/SciTEGlobal.properties.
The language specific properties files are also installed into this directory.

To remove SciTe
```sh
sudo make uninstall
```

To clean the object files which may be needed to change `$prefix`
```sh
make clean
```

The current make file supports static and dynamic linking between SciTe, Scintilla, and Lexilla.


### Windows version

A C++ 17 compiler is required.
Visual Studio 2019 is the development system used for most development
although Mingw-w64 9.2 is also supported.

To build Scintilla, make in the scintilla/win32 directory
```sh
cd scintilla\win32
# GCC:
mingw32-make
# Visual C++:
nmake -f scintilla.mak
```

```sh
cd ..\..
```

To build SciTe, use the makefiles located in the scite/win32 directory
```sh
cd scite\win32
# GCC:
mingw32-make
# Visual C++:
nmake -f scite.mak
```

An executable SciTE will now be in scite/bin.

### GTK+/Windows version

Mingw-w64 is known to work. Other compilers will probably not work.

Only Scintilla will build with GTK+ on Windows. SciTE will not work.

Make builds both a static library version of Scintilla with lexers (`scintilla.a`) and
a shared library without lexers (`libscintilla.so` or or `libscintilla.dll`).

To build Scintilla, make in the scintilla/gtk directory
```sh
cd scintilla\gtk
mingw32-make
```

### macOS Cocoa version

Xcode 9.2 or later may be used to build Scintilla on macOS.

There is no open source version of SciTe for macOS but there is a commercial
version available through the App Store.

To build Scintilla, run xcodebuild in the scintilla/cocoa/ScintillaFramework or 
scintilla/cocoa/Scintilla directory

```sh
cd cocoa/Scintilla
xcodebuild
```

### Qt version

See the qt/README file to build Scintilla with Qt.

#### License agreement for this project:

```
License for Lexilla, Scintilla, and SciTe

Copyright 1998-2021 by Neil Hodgson <neilh@scintilla.org>

All Rights Reserved 

Permission to use, copy, modify, and distribute this software and its 
documentation for any purpose and without fee is hereby granted, 
provided that the above copyright notice appear in all copies and that 
both that copyright notice and this permission notice appear in 
supporting documentation. 

NEIL HODGSON DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS 
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY 
AND FITNESS, IN NO EVENT SHALL NEIL HODGSON BE LIABLE FOR ANY 
SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES 
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, 
WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER 
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE 
OR PERFORMANCE OF THIS SOFTWARE. 
```

And here is the community license: <https://github.com/SciTe-Community/SciTe/blob/develop/LICENSE>.
