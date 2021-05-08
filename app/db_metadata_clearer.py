from app import db



try:
	db.metadata.clear("claimers") 
except InvalidRequestError:
	pass