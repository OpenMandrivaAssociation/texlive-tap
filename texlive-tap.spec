Name:		texlive-tap
Version:	31731
Release:	1
Summary:	TeX macros for typesetting complex tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/tables/tap077.zip
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a simple notation for pretty complex tables
(to Michael J. Ferguson's credit). With PostScript, the package
allows shaded/coloured tables, diagonal rules, etc. The package
is supposed to work with both Plain and LaTeX. An AWK converter
from ASCII semigraphic tables to TAP notation is included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tap
%doc %{_texmfdistdir}/doc/generic/tap

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
