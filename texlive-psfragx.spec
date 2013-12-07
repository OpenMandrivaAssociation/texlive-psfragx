# revision 26243
# category Package
# catalog-ctan /macros/latex/contrib/psfragx
# catalog-date 2012-05-07 20:30:54 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-psfragx
Version:	1.1
Release:	4
Summary:	A psfrag eXtension
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/psfragx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfragx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfragx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfragx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PSfragX offers a mechanism to embed \psfrag commands, as
provided by the psfrag package, into the EPS file itself. Each
time a graphic is included, the EPS file is scanned. If some
tagged lines are found, they are used to define the psfrag
replacements that should be performed automatically. In
addition, a similar mechanism holds for overpic objects. These
are picture objects superimposed on the included graphic. A
similar mechanism is implemented in psfrag itself (but
deprecated in the documentation), but psfragx offers much more
flexibility. For example, if babel is used, it is possible to
define different replacements corresponding to different
languages. The replacements to take into account will be
selected on the basis of the current language of the document.
A Matlab script (LaPrint) is provided, to export an EPS file
with psfragx annotations ready embedded.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/psfragx/psfragx.cfg
%{_texmfdistdir}/tex/latex/psfragx/psfragx.sty
%doc %{_texmfdistdir}/doc/latex/psfragx/README
%doc %{_texmfdistdir}/doc/latex/psfragx/README.laprint-3.16
%doc %{_texmfdistdir}/doc/latex/psfragx/laprint.m
%doc %{_texmfdistdir}/doc/latex/psfragx/laprintdoc.ps
%doc %{_texmfdistdir}/doc/latex/psfragx/laprpfx.mat
%doc %{_texmfdistdir}/doc/latex/psfragx/pfxprint.m
%doc %{_texmfdistdir}/doc/latex/psfragx/psfragx.m
%doc %{_texmfdistdir}/doc/latex/psfragx/psfragx.pdf
%doc %{_texmfdistdir}/doc/latex/psfragx/psfragx_example.pdf
%doc %{_texmfdistdir}/doc/latex/psfragx/psfragx_example.tex
%doc %{_texmfdistdir}/doc/latex/psfragx/readmePFX.txt
#- source
%doc %{_texmfdistdir}/source/latex/psfragx/psfragx.drv
%doc %{_texmfdistdir}/source/latex/psfragx/psfragx.dtx
%doc %{_texmfdistdir}/source/latex/psfragx/psfragx.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 805040
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-3
+ Revision: 787732
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755147
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719320
- texlive-psfragx
- texlive-psfragx
- texlive-psfragx
- texlive-psfragx

