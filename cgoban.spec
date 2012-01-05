Summary:	CGoban NNGS and IGS client
Summary(pl.UTF-8):	CGoban - klient NNGS i IGS
Name:		cgoban
Version:	1.9.14
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/cgoban1/%{name}-%{version}.tar.gz
# Source0-md5:	b360bc0374a1ee8b1fa296ad1c903bde
Source1:	%{name}.desktop
Source2:	%{name}_icon.png
# not maintained for 1.9.14
#Patch1:		http://goron.de/~froese/cgoban/cgoban-1.9.12-27.patch
URL:		http://cgoban1.sourceforge.net/
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGoban ("Complete Goban Mark 1") provides a large set of go-related
services for Unix and X11:
* Play go against another player.
* Edit and view SGF files.
* Connect to a go server over the internet. CGoban can connect to NNGS or IGS
  and gives a convenient graphical user interface to the server.
* Act as a bridge to go modem protocol.

%description -l pl.UTF-8
CGoban ("Complete Goban Mark 1") dostarcza narzędzi do gry w go. Między
innymi pozwala na:
* rozegranie partii z innym graczem
* edycję i przeglądanie plików SGF
* współpracę z serwerami NNGS i IGS. Dostarcza graficzny interfejs
  użytkownika dla tych protokołów

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
