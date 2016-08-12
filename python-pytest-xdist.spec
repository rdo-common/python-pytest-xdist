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
Version:        1.14
Release:        1%{?dist}
Summary:        py.test plugin for distributed testing and loop-on-failing modes

License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python2-setuptools_scm
BuildRequires:  python3-setuptools_scm

%description
%{desc}

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-execnet
Requires:       python2-pytest
Requires:       python2-py
%description -n python2-%{pypi_name}
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-execnet
Requires:       python3-pytest
Requires:       python3-py
%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install


%files -n python2-%{pypi_name}
%doc OVERVIEW.md README.rst
%license LICENSE
%{python2_sitelib}/pytest_xdist*
%{python2_sitelib}/xdist/

%files -n python3-%{pypi_name}
%doc OVERVIEW.md README.rst
%license LICENSE
%{python3_sitelib}/pytest_xdist*
%{python3_sitelib}/xdist/

%changelog
* Thu Aug 11 2016 Scott Talbert <swt@techie.net> - 1.14-1
- Initial package.
