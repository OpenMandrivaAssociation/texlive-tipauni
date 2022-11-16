Name:		texlive-tipauni
Version:	64774
Release:	1
Summary:	Producing Unicode characters with TIPA commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tipauni
License:	gpl3+ fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipauni.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipauni.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipauni.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Package TIPA uses the T3 encoding for producing IPA characters.
The package is widely used in the field of linguistics, but
because of the old encoding, the output documents are less
productive than Unicode-based documents. This package redefines
most of the TIPA-commands for outputting Unicode characters.
Users can now use their beloved TIPA shortcuts with the
benefits of Unicode, i.e. searchability, copy-pasting, changing
the font and many more. As this package needs the fontspec
package for loading an IPA font, it needs to be compiled with
XeLaTeX or LuaLaTeX. This package can also be viewed as an
ASCII-based input method for producing IPA characters in
Unicode. It needs the Charis SIL font for printing IPA
characters.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tipauni
%{_texmfdistdir}/tex/latex/tipauni
%doc %{_texmfdistdir}/doc/latex/tipauni

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
