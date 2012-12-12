package com.nofatclips.sieve;

public class TestSieve {
	
	public static void main (String args[]) {
		int n=2000000;
		Sieve s = new Sieve(n);
		long count=0;
		for (int i=0; i<=n; i++) if (s.isPrime(i)) count+=i;
		System.out.println(count);
	}
	
}