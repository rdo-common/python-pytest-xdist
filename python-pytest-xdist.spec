%global pypi_name pytest-xdist
%global desc The pytest-xdist plugin extends py.test with some unique test execution modes:\
* test run parallelization: if you have multiple CPUs or hosts you can use\
  those for a combined test run. This allows to speed up development or to use\
  special resources of remote machines.\
* --boxed: run each test in a boxed subprocess to survive SEGFAULTS or\
  otherwise dying processes\
* --looponfail: run your tests repeatedly in a subprocess. After each run\
  py.test waits until a file in your project changes and then re-runs the\
  previously failing tests. This is repeated until all tests pass after which\
  again a full run is performed.\
* Multi-Platform coverage: you can specify different Python interpreters or\
  different platforms and run tests in parallel on all of them.

Name:           python-%{pypi_name}
Version:        1.15.0
Release:        1.1%{?dist}
Summary:        py.test plugin for distributed testing and loop-on-failing modes

License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools_scm
BuildRequires:  python-setuptools

%description
%{desc}

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python-execnet
Requires:       pytest
Requires:       python-py
%description -n python2-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name}
%doc OVERVIEW.md README.rst
%license LICENSE
%{python2_sitelib}/pytest_xdist*
%{python2_sitelib}/xdist/

%changelog
* Mon Oct 03 2016 Scott Talbert <swt@techie.net> - 1.15.0-1
- New upstream release 1.15.0

* Thu Aug 11 2016 Scott Talbert <swt@techie.net> - 1.14-1
- Initial package.
