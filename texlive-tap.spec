%global tl_name tap
%global tl_revision 31731

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.77
Release:	%{tl_revision}.1
Summary:	TeX macros for typesetting complex tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/tables/tap077.zip
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a simple notation for pretty complex tables (to
Michael J. Ferguson's credit). With PostScript, the package allows
shaded/coloured tables, diagonal rules, etc. The package is supposed to
work with both Plain and LaTeX. An AWK converter from ASCII semigraphic
tables to TAP notation is included.

