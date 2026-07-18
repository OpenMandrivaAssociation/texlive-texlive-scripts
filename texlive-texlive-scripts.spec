%global tl_name texlive-scripts
%global tl_revision 79692
%global tl_bin_links fmtutil:%{_texmfdistdir}/scripts/texlive/fmtutil.pl fmtutil-sys:%{_texmfdistdir}/scripts/texlive/fmtutil-sys.sh fmtutil-user:%{_texmfdistdir}/scripts/texlive/fmtutil-user.sh man:%{_texmfdistdir}/doc/man mktexfmt:fmtutil mktexmf:%{_texmfdistdir}/scripts/texlive/mktexmf mktexpk:%{_texmfdistdir}/scripts/texlive/mktexpk mktextfm:%{_texmfdistdir}/scripts/texlive/mktextfm rungs:%{_texmfdistdir}/scripts/texlive/rungs.lua texhash:mktexlsr updmap:%{_texmfdistdir}/scripts/texlive/updmap.pl updmap-sys:%{_texmfdistdir}/scripts/texlive/updmap-sys.sh updmap-user:%{_texmfdistdir}/scripts/texlive/updmap-user.sh

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
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Includes install-tl, tl-portable, rungs, etc.; not needed for tlmgr to
run but still ours. Not included in tlcritical.

