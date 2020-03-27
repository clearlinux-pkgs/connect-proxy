#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : connect-proxy
Version  : 1
Release  : 16
URL      : http://localhost/cgit/projects/connect-proxy/snapshot/connect-proxy-1.tar.gz
Source0  : http://localhost/cgit/projects/connect-proxy/snapshot/connect-proxy-1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: connect-proxy-bin
Requires: connect-proxy-doc

%description
No detailed description available

%package bin
Summary: bin components for the connect-proxy package.
Group: Binaries

%description bin
bin components for the connect-proxy package.


%package doc
Summary: doc components for the connect-proxy package.
Group: Documentation

%description doc
doc components for the connect-proxy package.


%prep
%setup -q -n connect-proxy-1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510692615
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1510692615
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/connect-proxy

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
