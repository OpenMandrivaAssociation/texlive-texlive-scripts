%global tl_name texlive-scripts
%global tl_revision 79692

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX Live infrastructure programs
Group:		Publishing
URL:		https://www.ctan.org/pkg/texlive-scripts
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texlive-scripts.bin)
Requires:	texlive(texlive.infra)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Includes install-tl, tl-portable, rungs, etc.; not needed for tlmgr to
run but still ours. Not included in tlcritical.

