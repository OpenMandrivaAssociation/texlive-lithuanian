# revision 22722
# category Package
# catalog-ctan /language/lithuanian
# catalog-date 2008-11-06 00:30:15 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-lithuanian
Version:	20081106
Release:	3
Summary:	Lithuanian language support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/lithuanian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lithuanian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lithuanian.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/lithuanian/latin7x.enc
%{_texmfdistdir}/fonts/map/dvips/lithuanian/l7x-urwvn.map
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uagd.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uagdo.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uagk.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uagko.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ubkd.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ubkdi.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ubkl.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ubkli.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ucrb.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ucrbo.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ucrr.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-ucrro.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvbc.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvbo.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvboc.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvrc.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvro.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uhvroc.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uncb.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uncbi.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uncr.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uncri.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uplb.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uplr.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uplri.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-utmb.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-utmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-utmr.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-utmri.tfm
%{_texmfdistdir}/fonts/tfm/public/lithuanian/l7x-uzcmi.tfm
%{_texmfdistdir}/tex/latex/lithuanian/cp772.def
%{_texmfdistdir}/tex/latex/lithuanian/cp774.def
%{_texmfdistdir}/tex/latex/lithuanian/cp775.def
%{_texmfdistdir}/tex/latex/lithuanian/cpKBL.def
%{_texmfdistdir}/tex/latex/lithuanian/cpRIM.def
%{_texmfdistdir}/tex/latex/lithuanian/l7xenc.def
%{_texmfdistdir}/tex/latex/lithuanian/l7xenc.dfu
%{_texmfdistdir}/tex/latex/lithuanian/l7xenc.sty
%{_texmfdistdir}/tex/latex/lithuanian/l7xuag.fd
%{_texmfdistdir}/tex/latex/lithuanian/l7xubk.fd
%{_texmfdistdir}/tex/latex/lithuanian/l7xucr.fd
%{_texmfdistdir}/tex/latex/lithuanian/l7xuhv.fd
%{_texmfdistdir}/tex/latex/lithuanian/l7xunc.fd
%{_texmfdistdir}/tex/latex/lithuanian/l7xupl.fd
%{_texmfdistdir}/tex/latex/lithuanian/l7xutm.fd
%{_texmfdistdir}/tex/latex/lithuanian/l7xuzc.fd
%{_texmfdistdir}/tex/latex/lithuanian/latin7.def
%{_texmfdistdir}/tex/latex/lithuanian/lithuanian.ldf
%{_texmfdistdir}/tex/latex/lithuanian/lithuanian.sty
%doc %{_texmfdistdir}/doc/latex/lithuanian/COPYING
%doc %{_texmfdistdir}/doc/latex/lithuanian/ChangeLog
%doc %{_texmfdistdir}/doc/latex/lithuanian/Copyright
%doc %{_texmfdistdir}/doc/latex/lithuanian/README.lithuanian
%doc %{_texmfdistdir}/doc/latex/lithuanian/latin7lt.tex
%doc %{_texmfdistdir}/doc/latex/lithuanian/latin7x.etx
%doc %{_texmfdistdir}/doc/latex/lithuanian/latin7x.mtx
%doc %{_texmfdistdir}/doc/latex/lithuanian/latin7x.pdf
%doc %{_texmfdistdir}/doc/latex/lithuanian/makeLT.html
%doc %{_texmfdistdir}/doc/latex/lithuanian/makelt.tex
%doc %{_texmfdistdir}/doc/latex/lithuanian/makeltmap.tex
%doc %{_texmfdistdir}/doc/latex/lithuanian/testlt-urw.tex
%doc %{_texmfdistdir}/doc/latex/lithuanian/testlt.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081106-2
+ Revision: 753403
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081106-1
+ Revision: 718871
- texlive-lithuanian
- texlive-lithuanian
- texlive-lithuanian
- texlive-lithuanian

