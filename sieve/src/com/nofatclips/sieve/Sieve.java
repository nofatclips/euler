package com.nofatclips.sieve;

import java.util.BitSet;

public class Sieve {
	 
	private BitSet primes; // Inverse logic here: False means prime; True means non prime!
	private int top;
	
	public Sieve (int max) {
		this.top = max;
		this.primes = initSieve(max);
		filter();
	}
	
	// This function gives the expected result: false means non prime, true means prime
	public boolean isPrime (int n) {
		return !this.primes.get(n);
	}
	
	protected static BitSet initSieve(int max) {
		BitSet primes = new BitSet(max+6); // Allow 5 extra bits to avoid an if check in the last iteration of the for
		primes.set(0,2); // 0 and 1 are non primes
		primes.set(4); // 4 is not prime
		
		// Remove multiples of 2 and 3 in a single shot
		for (int index=6; index<=max; index+=6) {
			primes.set(index); // Multiples of 6 are definitely not prime
			primes.set(index+2,index+5); //Also numbers whose remainder of the division with 6 is 2,3 or 4 are not prime 
		}
		return primes;
	}
	
	protected void filter() {
		int prime=5;
		int maxPrime=(int) Math.floor(Math.sqrt(this.top));
		int nonPrime;
		while (prime<maxPrime) {
			for (nonPrime=prime*prime;nonPrime<=this.top;nonPrime+=2*prime) {
				this.primes.set(nonPrime);
			}
			prime = this.primes.nextClearBit(prime+2);
		}
	}

}
