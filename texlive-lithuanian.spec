Name:		texlive-lithuanian
Version:	46039
Release:	2
Summary:	Lithuanian language support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/lithuanian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lithuanian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lithuanian.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This language support package provides: - Lithuanian language
hyphenation patterns; - Lithuanian support for Babel; -
Lithuanian mapping and metrics for using the URW base-35 Type 1
fonts; - examples for making Lithuanian fonts with fontinst;
and - extra tools for intputenc and fontenc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/lithuanian
%{_texmfdistdir}/fonts/map/dvips/lithuanian
%{_texmfdistdir}/fonts/tfm/public/lithuanian
%{_texmfdistdir}/tex/latex/lithuanian
%doc %{_texmfdistdir}/doc/latex/lithuanian

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
