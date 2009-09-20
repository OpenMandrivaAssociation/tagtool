%define name	tagtool
%define version	0.12.3
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Audio file (MP3/OGG) tag editor
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/tagtool/%{name}-%{version}.tar.bz2
URL:		http://pwp.netcabo.pt/paol/tagtool/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig imagemagick
BuildRequires:	gtk2-devel libglade2.0-devel
BuildRequires:	id3lib-devel libvorbis-devel libogg-devel
BuildRequires:	perl-XML-Parser desktop-file-utils

%description
Audio Tag Tool is a program to manage the information fields in MP3 and Ogg
Vorbis files, commonly called tags.Tag Tool can be used to edit tags one by
one, but the most useful features are the ability to easily tag or rename
hundreds of files at once, in any desired format.  The mass tag and mass
rename features can handle filenames in any format thanks to an easily
configurable format template.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu

sed -i -e 's|False|false|g' %{buildroot}/%{_datadir}/applications/tagtool.desktop
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Audio;AudioVideoEditing" \
  --add-category="X-MandrivaLinux-Multimedia-Sound;AudioVideo" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/TagTool.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/TagTool.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/TagTool.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog README NEWS THANKS TODO
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/icons/hicolor/*
