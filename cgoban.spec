Summary:	CGoban NNGS and IGS client
Summary(pl):	CGoban - klient NNGS i IGS
Name:		cgoban
Version:	1.9.12
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://cgoban1.sourceforge.net/cgoban-%{version}.tar.gz
Patch0:		cgoban-configure-fix.patch
URL:		http://cgoban1.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
CGoban ("Complete Goban") 1 provides a large set of go-related
services for Unix and X11:
* Play go against another player.
* Edit and view SGF files.
* Connect to a go server over the internet. CGoban can connect to NNGS or IGS
  and gives a convienent graphical user interface to the server.
* Act as a bridge to go modem protocol.

%description -l pl
CGoban ("Complete Goban") 1 dostarcza narzêdzi dla gry w go. Miêdzy
innymi pozwala na:
* rozegranie partii z innym graczem
* edycjê i przegl±danie plików SGF
* wspó³pracê z serwerów NNGS i IGS. Dostarcza graficzny interfejs
  u¿ytkownika dla tych protoko³ów

%prep
%setup -q
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

install cgoban $RPM_BUILD_ROOT%{_bindir}
install man6/cgoban.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/cgoban.6*
