# randomread

Read a random subset of a text file in an efficient manner.

```python
from randomread import sample

# Read randomly picked 10-word snippet from a large text file
text = sample("large_textfile.txt", 10)
```

```python
# Read 100 randomly picked 2000-word chunks
text = sample("large_textfile.txt", 200000, chunk_size=2000)
```