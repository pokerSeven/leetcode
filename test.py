class xx(object):
	def dd(self):
		pre ,pre.next = self,2
		print self.next
		pre.next = 4
		print self.next

xx().dd()