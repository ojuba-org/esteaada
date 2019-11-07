Name: esteaada
Version: 2.1
Release: 1%{?dist}
Summary: Powerful file recovery
Summary(ar): مستعيد قوي للملفات
License: WAQF
URL: https://linuxac.org
Source0: %{name}-%{version}.tar.xz
Provides: ffe fhe
Requires: gtkdialog
Requires: polkit
Requires: udisks
Requires: foremost
Requires: util-linux
Requires: xterm
Buildarch: noarch

%description
File recovery program created to help in deleted file
recovery (normal delete or after format), very easily.

%description -l ar
برنامج لاستعادة الملفات المحذوفة حذفاً نهائياً سواء
كان ناتجاً عن عملية حذف طبيعي أو بعد تهيئة ، بشكل
مبسط وميسر .

%prep
%setup -q -n %{name}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp -pr languages types %{buildroot}%{_datadir}/%{name}

install -Dp -m 0755 %{name} %{buildroot}%{_bindir}
install -Dp -m 0755 ffe %{buildroot}%{_bindir}
install -Dp -m 0755 fhe %{buildroot}%{_bindir}
install -Dp -m 0755 %{name}.desktop %{buildroot}%{_datadir}/applications
install -Dp -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata
install -Dp -m 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps

%files
%license waqf2-ar.pdf
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_bindir}/ffe
%{_bindir}/fhe
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Nov 7 2019 Mosaab Alzoubi <moceap@hotmail.com> - 2.1-1
- Update to 2.1
- Many Fixes

* Sat Jan 28 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1.1-1
- Initial on Ojuba

* Tue Feb 21 2012 Mosaab Alzoubi <moceap@hotmail.com> - 1.1-1
- packed by Almohazzem 0.3.1 (simple RPM packager)
