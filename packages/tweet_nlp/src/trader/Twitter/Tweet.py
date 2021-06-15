class Tweet:
  """
  Wraps the data sent back with each tweet and gives helper methods for 
  working with the data
  """
  id = ''
  text = ''
  entities = dict()
  # Add more fields here if we change the request fields

  def __init__(self):
    pass
    

  def get_mentions(response):
    """
    TODO:
    Returns a unique set of users mentioned in any of
    the tweets so we can remove them from the dataset
    """
    print(response)

  def remove_mentions():
    """
    TODO:
    Removes tokens that are user @s since they shouldn't 
    contribute to our parsing
    """

  

  