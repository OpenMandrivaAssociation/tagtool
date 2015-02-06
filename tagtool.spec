Name: 	 	tagtool
Summary: 	Audio file (MP3/OGG) tag editor
Version: 	0.12.3
Release: 	5

Source:		http://prdownloads.sourceforge.net/tagtool/%{name}-%{version}.tar.bz2
URL:		http://pwp.netcabo.pt/paol/tagtool/
License:	GPL
Group:		Sound
BuildRequires:	pkgconfig imagemagick
BuildRequires:	pkgconfig(gtk+-2.0) libglade2.0-devel
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
export LDFLAGS="-logg -lm"
%configure2_5x
%make

%install
%makeinstall

#menu

sed -i -e 's|False|false|g' %{buildroot}/%{_datadir}/applications/tagtool.desktop
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Audio;AudioVideoEditing" \
  --add-category="X-MandrivaLinux-Multimedia-Sound;AudioVideo" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 pixmaps/TagTool.png %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 pixmaps/TagTool.png %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 pixmaps/TagTool.png %{buildroot}/%_miconsdir/%name.png

%find_lang %name

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


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.12.3-2mdv2010.0
+ Revision: 445346
- rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.12.3-1mdv2009.1
+ Revision: 332996
- New upstream release

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.12.2-2mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tvignaud@mandriva.com>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - import tagtool

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Sep 16 2006 Emmanuel Andry <eandry@mandriva.org> 0.12.2-2mdv2007.0
- %%mkrel
- xdg menu

* Sun May 29 2005 Austin Acton <austin@mandriva.org> 0.12.2-1mdk
- 0.12.2
- source URL

* Tue Feb 8 2005 Austin Acton <austin@mandrake.org> 0.12-1mdk
- initial package
