# revision 24220
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-scripts
Version:	20111104
Release:	1
Summary:	TeX Live infrastructure programs
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-texlive-scripts.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Includes install-tl, tl-portable, rungs, etc., not needed for
tlmgr to run but still ours.  Not included in tlcritical.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%{_datadir}/tlpkg/installer/install-menu-perltk.pl
%{_datadir}/tlpkg/installer/install-menu-text.pl
%{_datadir}/tlpkg/installer/install-menu-wizard.pl
%doc %{_mandir}/man1/install-tl.1*
%doc %{_texmfdir}/doc/man/man1/install-tl.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/texlive/rungs.tlu rungs
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
cp -fa install-tl %{buildroot}%{_tlpkgdir}
cp -fpar tlpkg/installer %{buildroot}%{_tlpkgdir}
