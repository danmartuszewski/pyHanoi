#!/usr/bin/python
#-*- coding: utf-8 -*-


class hanoi(object):
	u"""
	Hanoi to gra w której musisz przełożyć wszystkie krążki z palika A na palik C
	przestrzegając następujących zasad:
		1. Przenosisz krążek najwyżej położony na paliku.
		2. Nie możesz kłaść większego krążka na mniejszym.
	Paliki A, B, C są reprezentowane przez cyfry 1, 2, 3, a ich liczba jest stała.
	Przebieg gry:
		Na początku wybierasz liczbę krążków do przełożenia.
		Skąd: numer palika z którego chcesz przenieść najwyżej położony krązek
		Dokąd: numer palika na którym ten krążek zostanie położony, jeśli pamiętasz o zasadach
	Jeśli po wprowadzeniu pierwszej z liczb zauważyłeś, że wpisałeś ją błędnie
	wystarczy, że naciśniesz enter, by ponownie wprowadzić wartość. Taki ruch nie będzie 
	wliczony do ogólnej liczby ruchów.
	
	Dobrej zabawy!
	""" 
	def ustaw(self, ilKraz):
		u"""
		Metoda ustawia ilość krążków = ilKraz.
		Jej wywołanie jest niezbędne do rozpoczęcia gry
		"""
		self.ilKraz = ilKraz
		self.iRuchow = 0
		self.arr1 = []    # pierwszy palik
		self.arr2 = []    # drugi palik
		self.arr3 = []    # trzeci palik
		self.arrW = []    # palik wynikowy - używany do sprawdzenia czy gra została zakończona
		self.tabs = []    # tablica tablic(palików) z zerami w pustych miejscach. Wykorzystywana do graficznego przedstawienia stanu
		i = 1
		while i <= self.ilKraz:
			self.arr1.append(i)
			self.arrW.append(i)
			i+=1
	def pokaz(self):
		u"""
		@note
		Metoda przedstawiająca graficznie stan gry.
		"""
		self._zapelnij();     
		symbol = '++'     # symbol oznaczający krążek
		szerokosc = self.ilKraz *len(symbol) + 4  # szerokość palika
		for tab in zip(*self.tabs):   
			line = ''
			for el in tab:
				if el > 0:
					line += ('|' +  el * symbol + '|').center(szerokosc)       # krążki
				else:
					line += ' '.center(szerokosc)          # puste miejsca
			print line                                     # wyświetlenie jednej linii  
		print 'A'.center(szerokosc) + 'B'.center(szerokosc) + 'C'.center(szerokosc)       # podpisy palików
	def _zapelnij(self):
		self.tabs = [] 
		for arr in [self.arr1, self.arr2, self.arr3]:
			arrB = []
			l = len(arr)
			diff = self.ilKraz - l
			for x in range(diff):    # wypełnienie początkowych miejsc zerami
				try:
					arrB.append(0)
					#arrB.insert(len(arrB), arr[self.ilKraz-1-x])
				except IndexError: pass
			for x in range(l):       # skopiowanie wartości z oryginalnych tablic
				arrB.append(arr[x])
			self.tabs.append(arrB)
	def przesun(self, skad, dokad):
		u"""
		@return: 2 - Usiłowano ustawić większy krążek na mniejszym
		@return: 3 - Palik skad był pusty
		@note 
		Metoda przesuwa krążki z palika skad do dokad.
		Dozwolone parametry to 1, 2 lub 3.
		Reprezentują one kolejno paliki A, B lub C
		"""
		if skad == 1: skad = self.arr1        # przypisanie wskaźników
		elif skad == 2:	skad = self.arr2
		else: skad = self.arr3
		if dokad == 1: dokad = self.arr1
		elif dokad == 2: dokad = self.arr2
		else: dokad = self.arr3
		if len(skad) > 0: 
			if len(dokad) == 0 or (len(dokad) > 0 and skad[0] < dokad[0]):   # jeśli ruch jest zgodny z zasadami
				dokad.insert(0, skad.pop(0))                                 # krążek zostaje przeniesiony
				self.iRuchow += 1                                           
			else:
			    return 2
		else:
			return 3
	def sprawdz(self):
		u"""
		@return: boolean
		@note:
		Metoda sprawdza, czy gra została zakończona.
		Jeśli tak - zwraca True
		"""
		if self.arr3 == self.arrW:
			return True
		return False