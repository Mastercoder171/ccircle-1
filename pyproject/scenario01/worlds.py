def easy():
  return '''
    X-W---
    --WWWW
    --W---
    W---W-
    ---WW-
    WWWW!-
  '''

def medium():
  return '''
    -W-W-W-W-W
    ----------
    -WWWWWWW--
    -W------W-
    -W-WWWW-W-
    -W-WX---W-
    -W-WWWW-W-
    -W-----W!-
    -WWWWW-W-W
    -------W-W
  '''

def hard():
  s = '''
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    C   |     |     | |         |   |     |   |   |     | |     |
    + +-+ + + + +-+ + + +-+-+ + +-+ + +-+ +-+ + + + +-+ + + +-+ +
    |     | | | |   | | |   | | |   |   |   |   | | |   |   |   |
    +-+-+-+ + + + +-+ + + +-+ + + + + +-+-+ +-+-+ + + +-+-+-+ +-+
    |   | | | | | |     |     |   | | |   | |     | | |         |
    + + + + + +-+ +-+ +-+-+-+-+-+-+ + + +-+ + +-+-+ + + +-+-+-+ +
    | |   | |   |   |   |             |     |   |   |         | |
    + +-+-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+-+-+-+ +-+ +-+-+ +-+-+ + +
    |       |   |   | |   |   | | | |   |     |   |     |   | | |
    +-+-+-+-+ +-+ +-+ +-+ +-+ + + + + + + + +-+ +-+ +-+-+ +-+ + +
    |     |   |     |     |   |   | | | | |   |   |     |   | | |
    + +-+ + +-+ +-+ + +-+-+ +-+-+-+ + + + +-+ +-+ +-+-+ +-+ + + +
    |   | | |   |   |   |   |         | | |     |   |   | |   | |
    +-+ +-+ + +-+ +-+-+ + +-+ +-+-+ +-+ + +-+-+ +-+ + +-+ +-+-+ +
    |       | |   |     | |   | |   | | |     |   | |   | |     |
    + +-+-+ + + +-+ +-+-+ + + + + +-+ + +-+-+ +-+ + +-+ + + +-+-+
    | |     | |   |   |   | | |   |   |   |   |   | |   | | |   |
    + + +-+-+ +-+ +-+ + +-+ +-+-+-+ +-+ +-+ +-+ +-+ + +-+ + +-+ +
    | | |       | |   | |   |     | |       |     | |     |     |
    + + +-+-+-+ + + +-+ +-+-+ +-+ + +-+-+-+-+-+-+ + +-+-+-+-+-+ +
    | |         |   | | |   |   |     |       |   | |   |   |   |
    + +-+-+-+-+-+-+-+ + + + +-+ +-+-+ + +-+-+ +-+ + + + +-+ + +-+
    | |       |     | | | |   |     | | | |   |   |   | |   | | |
    + +-+-+-+ + +-+ + + + + + +-+ +-+ + + + +-+ +-+-+-+ + +-+ + +
    | |   |   |   |   |   | |   |   |     | |   |       |     | |
    + + + + +-+-+ +-+-+-+-+ + + +-+ +-+-+-+ + +-+ +-+-+-+-+-+-+ +
    |   |       |     |   | | |   | |     | |     |   |       | |
    +-+-+-+ + +-+-+-+ + + + + +-+ + + +-+ + +-+-+-+ + + +-+ +-+ +
    |   |   |       | | | | | |   | |   | |     |   | |   |   | |
    +-+ + +-+-+-+-+ + + + + +-+ +-+ +-+ +-+-+-+ + +-+ +-+ +-+ + +
    |   | |         |   | |   | |     |         |   | |   |   | |
    + +-+ + +-+-+-+-+-+ +-+ + + + +-+-+-+-+-+-+-+-+ + +-+-+ + + +
    |     | |   |           | | |         |     |   |   |   | | |
    +-+-+-+ + + + +-+ +-+-+-+ +-+-+-+ +-+-+ + + +-+-+-+ +-+-+ + +
    |       | |     |     | | |       |   | | |   |     |     | |
    + +-+-+-+-+-+-+ +-+-+ + + + +-+-+-+ + +-+ +-+ + +-+-+ +-+-+ +
    | |       | |   |     |   |       | |   | |     |     |     |
    + +-+-+-+ + + +-+ +-+-+ +-+-+ +-+ + +-+ + +-+ +-+ +-+-+ +-+-+
    |         |   | | |   |       |   |   | |   |       |   |   |
    +-+-+-+-+-+ +-+ + +-+ +-+-+-+-+ +-+-+ + +-+ +-+-+ + + +-+ + +
    |           |         |       | |     |   |   |   |   |   | |
    + +-+-+-+-+-+-+-+ +-+-+ + +-+ + +-+ +-+-+ +-+ + +-+-+-+ +-+ +
    |     |       | |       | |   |   |   |     | |     |     | |
    +-+-+ + +-+-+ + +-+-+-+-+-+ + +-+ +-+ + +-+-+ +-+-+ + +-+-+ +
    | |   |   | | |             |   | |   |       |     | |     |
    + + +-+-+ + + + +-+-+-+-+-+-+-+-+ + +-+-+-+-+-+ +-+-+ +-+-+-+
    |   | |   |   | |               |   |   |   |   |   |   |   |
    +-+-+ + +-+-+ + +-+-+-+-+-+-+-+ +-+-+ + + +-+ +-+-+ +-+ + + +
    |   | |   |   |   |           | |     |       |   | |   | | |
    + + + +-+ + +-+-+ + +-+-+-+-+ + + +-+-+-+-+-+-+ + + + +-+-+ +
    | | |     |       |   |   | |   |     |         |   | |   | |
    +-+ +-+-+-+-+ +-+-+-+ + + + +-+-+-+-+ + +-+ +-+-+-+-+ + + + +
    |   |       |         | | |       |   |   | |         | | | |
    + +-+ +-+-+ +-+-+ +-+-+ + +-+-+-+ + +-+-+ + + +-+ + +-+-+ + +
    |   |     |           | |     |   | |     | | |   |   |     |
    +-+ +-+ +-+-+-+-+-+ + + + +-+ + +-+ + +-+-+ + + +-+-+ + + + +
    |       |     |   | | | | |   | |   |   |   | |     |   | | |
    + +-+-+-+ +-+ + +-+ + + + + +-+ + + +-+ + +-+-+-+-+ +-+-+ + +
    |         |   |     |   | |     | |     |           |     | P
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  '''

  s = '\n'.join([x.strip() for x in s.strip().split('\n')])
  s = s.replace('+', 'W')
  s = s.replace('-', 'W')
  s = s.replace('|', 'W')
  return s