Name:           hyprlock
Version:        0.4.0
Release:        1
Summary:        Hyprland's GPU-accelerated screen locking utility
License:        BSD-3-Clause
Group:          Utility/Hyprland
URL:            https://github.com/hyprwm/hyprlock
Source0:        https://github.com/hyprwm/hyprlock/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
Hyprland's simple, yet multi-threaded and GPU-accelerated screen locking utility.
Features:

    - uses the secure ext-session-lock protocol
    - full support for fractional-scale
    - fully GPU accelerated
    - multi-threaded resource acquisition for no hitches


%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
