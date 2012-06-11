# revision 26286
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-scripts
Version:	20120611
Release:	1
Summary:	TeX Live infrastructure programs
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texlive-scripts.bin = %{EVRD}

%description
Includes install-tl, tl-portable, rungs, etc., not needed for
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
%{_tlpkgdir}/install-tl
%{_texmfdir}/scripts/texlive/lua/texlive/getopt.tlu
%{_texmfdir}/scripts/texlive/lua/texlive/tlpdb.tlu
%{_texmfdir}/scripts/texlive/lua/texlive/utils.tlu
%{_texmfdir}/scripts/texlive/rungs.tlu
%{_texmfdir}/scripts/texlive/test-tlpdb.tlu
%{_texmfdir}/scripts/texlive/texconf.tlu
%{_tlpkgdir}/installer/ctan-mirrors.pl
%{_tlpkgdir}/installer/install-menu-perltk.pl
%{_tlpkgdir}/installer/install-menu-text.pl
%{_tlpkgdir}/installer/install-menu-wizard.pl
%doc %{_mandir}/man1/install-tl.1*
%doc %{_texmfdir}/doc/man/man1/install-tl.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/texlive/rungs.tlu rungs
popd
mkdir -p %{buildroot}%{_tlpkgdir}
cp -fa install-tl %{buildroot}%{_tlpkgdir}
cp -fpar tlpkg/installer %{buildroot}%{_tlpkgdir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
