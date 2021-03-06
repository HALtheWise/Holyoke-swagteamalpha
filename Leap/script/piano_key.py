# ###############################################################################
# HackHolyoke - PianoPianoRevolution                                            #
# Keyboard projection map for Leap Motion which stores the database of          #
# locations for all the keys and reports whether a strike is in a specific key's#
# boundaries  																	#
#                                                                               #
# Created by Kevin Zhang and Kimberly Winter                                    #
# ###############################################################################

class piano_key():
	"""
	creates a key with boundaries and a function to check if it has been hit
	"""

	def __init__(self, x1Bound,x2Bound, z1Bound, z2Bound):
		self.x1Bound=x1Bound  #the boundaries of the key (each key can be defined as a rectangle)
		self.x2Bound=x2Bound  #bound 1 is the lesser boundarx
		self.z1Bound=z1Bound
		self.z2Bound=z2Bound

	def is_pressed(self, bone):
		if(bone.next_joint.x>self.x1Bound and bone.next_joint.x<self.x2Bound and bone.next_joint.z>self.z1Bound and bone.next_joint.z<self.z2Bound): ##and bone.next_joint.z
			return True
		else:
			return False

#creates all the keys in a two octave range around middle C
def create_piano_keys():
	keyF3=piano_key(-214, -155, 5, 70)
	keyF32=piano_key(-214, -191, -105, 5)
	keyF3sharp=piano_key(-191, -177, -105, 5)
	keyG3=piano_key(-155, -135, 5, 70)
	keyG32=piano_key(-177, -167, -105, 5)
	keyG3sharp=piano_key(-167, -147, -105, 5)
	keyA3=piano_key(-135, -110, 5, 70)
	keyA32=piano_key(-147, -133, -105, 5)
	keyA3sharp=piano_key(-133, -117, -105, 5)
	keyB3=piano_key(-110, -90, 5, 70)
	keyB32=piano_key(-117, -98, -105, 5)
	keyC4=piano_key(-90, -60, 5, 70)
	keyC42=piano_key(-98, -79, -105, 5)
	keyC4sharp=piano_key(-79, -53, -105, 5)
	keyD4=piano_key(-60, -33, 5, 70)
	keyD42=piano_key(-53, -45, -105, 5)
	keyD4sharp=piano_key(-45, -22, -105, 5)
	keyE4=piano_key(-33, -6, 5, 70)
	keyE42=piano_key(-22, -6, -105, 5)
	keyF4=piano_key(-6, 20, 5, 70)
	keyF42=piano_key(-6, 15, -105, 5)
	keyF4sharp=piano_key(15, 37, -105, 5)
	keyG4=piano_key(20, 50, 5, 70)
	keyG42=piano_key(37, 48, -105, 5)
	keyG4sharp=piano_key(48, 68, -105, 5)
	keyA4=piano_key(50, 70, 5, 70)
	keyA42=piano_key(68, 78, -105, 5)
	keyA4sharp=piano_key(78, 102, -105, 5)
	keyB4=piano_key(70, 100, 5, 70)
	keyB42=piano_key(102, 120, -105, 5)
	keyC5=piano_key(100, 130, 5, 70)
	keyC52=piano_key(120, 141, -105, 5)
	keyC5sharp=piano_key(141, 160, -105, 5)
	keyD5=piano_key(130, 160, 5, 70)
	keyD52=piano_key(160, 175, -105, 5)
	keyD5sharp=piano_key(175, 195, -105, 5)
	keyE5=piano_key(160, 213, 5, 70)
	keyE52=piano_key(195, 213, -105, 5)



	return [keyF3, keyF32, keyF3sharp, keyG3, keyG32, keyG3sharp, keyA3, keyA32, keyA3sharp, keyB3, keyB32, keyC4,
			keyC42, keyC4sharp, keyD4, keyD42, keyD4sharp, keyE4, keyE42, keyF4, keyF42, keyF4sharp, keyG4, keyG42, keyG4sharp, keyA4, keyA42, keyA4sharp, keyB4, keyB42, keyC5, keyC52, keyC5sharp, keyD5, keyD52,
			keyD5sharp, keyE5, keyE52]
