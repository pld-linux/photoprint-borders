Summary:	Photo Print - Prints photos in various layouts and with color management
Name:		photoprint-borders
Version:	0.0.2
Release:	0.1
License:	GPL
Group:		Publishing
Source0:	http://www.blackfiveservices.co.uk/photoprint_resources/%{name}-%{version}.tar.gz
# Source0-md5:	6c9b557eb616032f2be7f0178b499e71
URL:		http://www.blackfiveservices.co.uk/photoprint.shtml
Requires:	photoprint
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image frames (Templates in /usr/share/photoprint/borders/) and color
management (Profiling instructions in
/usr/share/photoprint/ProfilingKit/ProfilingKit.html).
Photo Print can be used as GUI tool and also as command line tool in
batch mode.
Works nicely as an image editor in GQ-View.

%prep
%setup -q 

%build
%{configure}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/photoprint/borders/*.tif
