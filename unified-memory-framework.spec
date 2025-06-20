#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: cd8d006
#
%define keepstatic 1
Name     : unified-memory-framework
Version  : 0.12.0.dev2
Release  : 8
URL      : https://github.com/oneapi-src/unified-memory-framework/archive/v0.12.0-dev2/unified-memory-framework-0.12.0-dev2.tar.gz
Source0  : https://github.com/oneapi-src/unified-memory-framework/archive/v0.12.0-dev2/unified-memory-framework-0.12.0-dev2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: unified-memory-framework-lib = %{version}-%{release}
Requires: unified-memory-framework-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : google-benchmark
BuildRequires : googletest
BuildRequires : pkg-config
BuildRequires : pkgconfig(hwloc)
BuildRequires : pkgconfig(jemalloc)
BuildRequires : pkgconfig(level-zero)
BuildRequires : pkgconfig(libze_loader)
BuildRequires : pkgconfig(numa)
BuildRequires : pkgconfig(tbb)
BuildRequires : pkgconfig(valgrind)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Unified Memory Framework
[![PR/push](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/pr_push.yml/badge.svg?branch=main&event=push)](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/pr_push.yml)
[![Coverage](https://gist.githubusercontent.com/bb-ur/3f66c77d7035df39aa75dda8a2ac75b3/raw/umf_coverage_badge.svg)](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/pr_push.yml?query=branch%3Amain)
[![GitHubPages](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/docs.yml)
[![Nightly](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/nightly.yml/badge.svg?branch=main)](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/nightly.yml)
[![Coverity build](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/coverity.yml/badge.svg?branch=main)](https://github.com/oneapi-src/unified-memory-framework/actions/workflows/coverity.yml)
[![Coverity report](https://scan.coverity.com/projects/29761/badge.svg?flat=0)](https://scan.coverity.com/projects/oneapi-src-unified-memory-framework)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/oneapi-src/unified-memory-framework/badge)](https://securityscorecards.dev/viewer/?uri=github.com/oneapi-src/unified-memory-framework)

%package dev
Summary: dev components for the unified-memory-framework package.
Group: Development
Requires: unified-memory-framework-lib = %{version}-%{release}
Provides: unified-memory-framework-devel = %{version}-%{release}
Requires: unified-memory-framework = %{version}-%{release}

%description dev
dev components for the unified-memory-framework package.


%package doc
Summary: doc components for the unified-memory-framework package.
Group: Documentation

%description doc
doc components for the unified-memory-framework package.


%package lib
Summary: lib components for the unified-memory-framework package.
Group: Libraries
Requires: unified-memory-framework-license = %{version}-%{release}

%description lib
lib components for the unified-memory-framework package.


%package license
Summary: license components for the unified-memory-framework package.
Group: Default

%description license
license components for the unified-memory-framework package.


%prep
%setup -q -n unified-memory-framework-0.12.0-dev2
cd %{_builddir}/unified-memory-framework-0.12.0-dev2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749246798
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
-DUMF_BUILD_CUDA_PROVIDER=OFF \
-DUMF_BUILD_GPU_EXAMPLES=ON \
-DUMF_BUILD_LEVEL_ZERO_PROVIDER=ON \
-DUMF_BUILD_LIBUMF_POOL_DISJOINT=ON \
-DUMF_BUILD_SHARED_LIBRARY=ON \
-DUMF_BUILD_TESTS=OFF \
-DUMF_LEVEL_ZERO_INCLUDE_DIR=/usr/include/level_zero  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749246798
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unified-memory-framework
cp %{_builddir}/unified-memory-framework-0.12.0-dev2/LICENSE.TXT %{buildroot}/usr/share/package-licenses/unified-memory-framework/64be5dda96ce5bef89d87aec325a52135dc3b6e2 || :
cp %{_builddir}/unified-memory-framework-0.12.0-dev2/licensing/third-party-programs.txt %{buildroot}/usr/share/package-licenses/unified-memory-framework/9de68a35905bcadf7bc3916654fb5f7a2b717d68 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/umf.h
/usr/include/umf/base.h
/usr/include/umf/ipc.h
/usr/include/umf/memory_pool.h
/usr/include/umf/memory_pool_ops.h
/usr/include/umf/memory_provider.h
/usr/include/umf/memory_provider_gpu.h
/usr/include/umf/memory_provider_ops.h
/usr/include/umf/mempolicy.h
/usr/include/umf/memspace.h
/usr/include/umf/memtarget.h
/usr/include/umf/pools/pool_disjoint.h
/usr/include/umf/pools/pool_jemalloc.h
/usr/include/umf/pools/pool_proxy.h
/usr/include/umf/pools/pool_scalable.h
/usr/include/umf/providers/provider_cuda.h
/usr/include/umf/providers/provider_devdax_memory.h
/usr/include/umf/providers/provider_file_memory.h
/usr/include/umf/providers/provider_fixed_memory.h
/usr/include/umf/providers/provider_level_zero.h
/usr/include/umf/providers/provider_os_memory.h
/usr/include/umf/proxy_lib_new_delete.h
/usr/lib64/cmake/umf/umf-config-version.cmake
/usr/lib64/cmake/umf/umf-config.cmake
/usr/lib64/cmake/umf/umf-targets-relwithdebinfo.cmake
/usr/lib64/cmake/umf/umf-targets.cmake
/usr/lib64/libumf.so
/usr/lib64/libumf_proxy.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/umf/LICENSE.TXT
/usr/share/doc/umf/examples/CMakeLists.txt
/usr/share/doc/umf/examples/README.md
/usr/share/doc/umf/examples/basic/CMakeLists.txt
/usr/share/doc/umf/examples/basic/basic.c
/usr/share/doc/umf/examples/cmake/FindCUDA.cmake
/usr/share/doc/umf/examples/cmake/FindJEMALLOC.cmake
/usr/share/doc/umf/examples/cmake/FindLIBHWLOC.cmake
/usr/share/doc/umf/examples/cmake/FindLIBNUMA.cmake
/usr/share/doc/umf/examples/cmake/FindLIBUMF.cmake
/usr/share/doc/umf/examples/cmake/FindTBB.cmake
/usr/share/doc/umf/examples/cmake/FindZE_LOADER.cmake
/usr/share/doc/umf/examples/common/examples_level_zero_helpers.c
/usr/share/doc/umf/examples/common/examples_level_zero_helpers.h
/usr/share/doc/umf/examples/common/examples_utils.h
/usr/share/doc/umf/examples/cuda_shared_memory/CMakeLists.txt
/usr/share/doc/umf/examples/cuda_shared_memory/cuda_shared_memory.c
/usr/share/doc/umf/examples/custom_file_provider/CMakeLists.txt
/usr/share/doc/umf/examples/custom_file_provider/custom_file_provider.c
/usr/share/doc/umf/examples/dram_and_fsdax/CMakeLists.txt
/usr/share/doc/umf/examples/dram_and_fsdax/dram_and_fsdax.c
/usr/share/doc/umf/examples/ipc_ipcapi/CMakeLists.txt
/usr/share/doc/umf/examples/ipc_ipcapi/ipc_ipcapi_anon_fd.sh
/usr/share/doc/umf/examples/ipc_ipcapi/ipc_ipcapi_consumer.c
/usr/share/doc/umf/examples/ipc_ipcapi/ipc_ipcapi_producer.c
/usr/share/doc/umf/examples/ipc_ipcapi/ipc_ipcapi_shm.sh
/usr/share/doc/umf/examples/ipc_level_zero/CMakeLists.txt
/usr/share/doc/umf/examples/ipc_level_zero/ipc_level_zero.c
/usr/share/doc/umf/examples/level_zero_shared_memory/CMakeLists.txt
/usr/share/doc/umf/examples/level_zero_shared_memory/level_zero_shared_memory.c
/usr/share/doc/umf/examples/memspace_hmat/CMakeLists.txt
/usr/share/doc/umf/examples/memspace_hmat/memspace_hmat.c
/usr/share/doc/umf/examples/memspace_numa/CMakeLists.txt
/usr/share/doc/umf/examples/memspace_numa/memspace_numa.c
/usr/share/doc/umf/licensing/third-party-programs.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/libumf.so.0
/usr/lib64/libumf.so.0.0.0
/usr/lib64/libumf_proxy.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/unified-memory-framework/64be5dda96ce5bef89d87aec325a52135dc3b6e2
/usr/share/package-licenses/unified-memory-framework/9de68a35905bcadf7bc3916654fb5f7a2b717d68
