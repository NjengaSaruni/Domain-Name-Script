import pythonwhois

def available(firstnames=None, lastnames=None):
	available = set()
	for firstname in firstnames:
		for lastname in lastnames:
			domain = '{}{}{}'.format(firstname, lastname, '.com')
			inv_domain = '{}{}{}'.format(lastname, firstname, '.com')
			print 'Trying... ' + domain
			if pythonwhois.get_whois(domain)['contacts']['admin'] is None:
				print 'Available: ' + domain 
			print 'Trying... ' + inv_domain
			if pythonwhois.get_whois(inv_domain)['contacts']['admin'] is None:
				print 'Available: ' + inv_domain

	print available