%global tl_name lithuanian
%global tl_revision 66461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Lithuanian language support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/lithuanian
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lithuanian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lithuanian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This language support package provides: extra 8-bit encoding L7x used by
fontenc: l7xenc.def, l7xenc.dfu, l7xenc.sty Lithuanian TeX support for
URW family Type1 fonts: map, fd, tfm with L7x encoding extra code page
definitions used by inputenc: cp775.def, latin7.def

