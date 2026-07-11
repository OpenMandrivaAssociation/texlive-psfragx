%global tl_name psfragx
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A psfrag eXtension
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/psfragx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psfragx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psfragx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psfragx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PSfragX offers a mechanism to embed \psfrag commands, as provided by the
psfrag package, into the EPS file itself. Each time a graphic is
included, the EPS file is scanned. If some tagged lines are found, they
are used to define the psfrag replacements that should be performed
automatically. In addition, a similar mechanism holds for overpic
objects. These are picture objects superimposed on the included graphic.
A similar mechanism is implemented in psfrag itself (but deprecated in
the documentation), but psfragx offers much more flexibility. For
example, if babel is used, it is possible to define different
replacements corresponding to different languages. The replacements to
take into account will be selected on the basis of the current language
of the document. A Matlab script (LaPrint) is provided, to export an EPS
file with psfragx annotations ready embedded.

