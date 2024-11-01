Name:		texlive-texlive-scripts
Version:	72673
Release:	1
Summary:	TeX Live infrastructure programs
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texlive-scripts.bin = %{EVRD}

%description
Includes install-tl, tl-portable, rungs, etc.; not needed for
tlmgr to run but still ours.  Not included in tlcritical.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/rungs
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_tlpkgdir}/install-tl
%{_tlpkgdir}/installer
%{_texmfdistdir}/dvips/tetex
%{_texmfdistdir}/fonts
%{_texmfdistdir}/scripts
%{_texmfdistdir}/web2c
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/man/man5/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texlive/rungs.tlu rungs
popd
mkdir -p %{buildroot}%{_tlpkgdir}
cp -fa install-tl %{buildroot}%{_tlpkgdir}
cp -fpar tlpkg/installer %{buildroot}%{_tlpkgdir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

# This used to be in texlive-tetex along with the corresponding symlinks.
# Let's add the symlinks so stuff made for tetex can still find it all...
ln -s %{_texmfdistdir}/scripts/texlive/fmtutil.pl %{buildroot}%{_bindir}/fmtutil
ln -s %{_texmfdistdir}/scripts/texlive/fmtutil-sys.sh %{buildroot}%{_bindir}/fmtutil-sys
ln -s %{_texmfdistdir}/scripts/texlive/updmap.pl %{buildroot}%{_bindir}/updmap
ln -s %{_texmfdistdir}/scripts/texlive/updmap-sys.sh %{buildroot}%{_bindir}/updmap-sys
