# spec file for package nodejs-nodejs-deep-equal
%{?scl:%scl_package nodejs-nodejs-deep-equal}
%{!?scl:%global pkg_name %{name}}

%global npm_name deep-equal
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-deep-equal
Version:	1.0.0
Release:	1%{?dist}
Summary:	node's assert.deepEqual algorithm
Url:		https://github.com/substack/node-deep-equal
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tape)
%endif

%description
node's assert.deepEqual algorithm

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js lib \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tape test/*.js
%endif

%files
%{nodejs_sitelib}/deep-equal

%doc readme.markdown
%license LICENSE

%changelog
* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-1
- Initial build
