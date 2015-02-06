Name:		bfast
Version:	0.7.0a
Release:	3
Summary:	Blat-like Fast Accurate Search Tool

Group:		Sciences/Physics
License:	GPLv2 and MIT
URL:		http://bfast.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	zlib-devel bzip2-devel

%description

BFAST facilitates the fast and accurate mapping of short reads to
reference sequences.  Some advantages of BFAST include:

Speed: enables billions of short reads to be mapped quickly.

Accuracy: A priori probabilities for mapping reads with defined set of
variants.

An easy way to measurably tune accuracy at the expense of speed.

Specifically, BFAST was designed to facilitate whole-genome
resequencing, where mapping billions of short reads with variants is
of utmost importance.

BFAST supports both Illumina and ABI SOLiD data, as well as any other
Next-Generation Sequencing Technology (454, Helicos), with particular
emphasis on sensitivity towards errors, SNPs and especially
indels. Other algorithms take short-cuts by ignoring errors, certain
types of variants (indels), and even require further alignment, all to
be the "fastest" (but still not complete). BFAST is able to be tuned
to find variants regardless of the error-rate, polymorphism rate, or
other factors.


%prep
%setup -q

# temporary fix for 32-bit build problem
sed -i '/^extended_CFLAGS=/ s/-m64//' configure

%build
%configure
%make

%install
%makeinstall_std

rm %{buildroot}/%{_docdir}/%{name}/LICENSE
rm %{buildroot}/%{_docdir}/%{name}/bfast-book.pdf


%files
%doc AUTHORS ChangeLog NEWS README LICENSE
%doc manual/bfast-book.pdf
%{_bindir}/balignmentscoredistribution
%{_bindir}/balignsim
%{_bindir}/bevalsim
%{_bindir}/bfast
%{_bindir}/bfast.resubmit.pl
%{_bindir}/bfast.submit.pl
%{_bindir}/bgeneratereads
%{_bindir}/bindexdist
%{_bindir}/bindexhist
%{_bindir}/bmfmerge
%{_bindir}/brepeat
%{_bindir}/btestindexes
%{_bindir}/ill2fastq.pl
%{_bindir}/solid2fastq


%changelog
* Mon Nov 28 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.7.0a-1
+ Revision: 734971
- imported package bfast

