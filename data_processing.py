# Importing all relevant Python modules and libraries
import os
import json
import classla
import re

# Importing the Classla natural langauge processing pipeline for the standard version of Slovene
nlp = classla.Pipeline('sl', type='standard')

# Opening and writing to the .vert file
# Note 1: the program opens a new file if no .vert file with this name exists previously,
# if such a file exsists the program ends
# Note 2: The scraped text is being read from two separate .json files
path = 'r_slovenia_processed_text.vert'
if not os.path.exists(path):    
    with open(path, 'w', encoding='utf-8') as file:
        # Processing of text scraped from posts
        with open('posts.json', 'r', encoding='utf-8') as post_file:
            data = json.load(post_file)
            for post in data:
                row = []
                metadata = []
                if 'post_title' in data[post]:
                    # Splitting source text
                    split_text = re.split(r'(?<=[.!?] )', data[post]['post_title'])
                    for i in range(0, len(split_text)):
                        text = split_text[i].strip()
                        # Processing split text
                        processed = nlp(text)
                        conll_processed = processed.to_conll()
                        row.append(conll_processed)
                else:
                    row.append('N/A')
                if 'post_author' in data[post]:
                    metadata.append(f'Anonymous{int(post) + 1}')
                else:
                    metadata.append(f'Anonymous{int(post) + 1}')
                if 'date' in data[post]:
                    metadata.append(data[post]['date'])
                else:
                    metadata.append('N/A')
                if 'comments' in data[post]:
                    metadata.append(data[post]['comments'])
                else:
                    metadata.append('N/A')
                if 'votes' in data[post]:
                    metadata.append(data[post]['votes'])
                else:
                    metadata.append('N/A')
                if 'post_text' in data[post]:
                    # Splitting source text
                    split_text = re.split(r'(?<=[.!?] )', data[post]['post_text'])
                    for i in range(0, len(split_text)):
                        text = split_text[i].strip()
                        # Processing split text
                        processed = nlp(text)
                        conll_processed = processed.to_conll()
                        row.append(conll_processed)

                # Writing processed post-text and relevant metadata to the .vert file
                file.write(f'<doc source="r/Slovenia" text_type="post" author="{metadata[0]}" date="{metadata[1]}" comments="{metadata[2]}" votes="{metadata[3]}">' + '\n')
                for i in range(0, len(row)):
                    file.write('<s>' + '\n')
                    file.write(row[i] + '\n')
                    file.write('</s>' + '\n')
                file.write('</doc>' + '\n')

        # Processing of text scraped from comments and replies
        with open('comments_and_replies.json', 'r', encoding='utf-8') as comment_file:
            data = json.load(comment_file)
            for comment in data:
                row = []
                metadata = []
                if 'comment_author' in data[comment]:
                    metadata.append(f'Anonymous{int(comment) + 1}')
                else:
                    metadata.append(f'Anonymous{int(comment) + 1}')
                if 'comment_text' in data[comment]:
                    # Splitting source text
                    split_text = re.split(r'(?<=[.!?] )', data[comment]['comment_text'])
                    for i in range(0, len(split_text)):
                        text = split_text[i].strip()
                        # Processing split text
                        processed = nlp(text)
                        conll_processed = processed.to_conll()
                        row.append(conll_processed)
                
                # Writing processed comment-text and relevant metadata to the .vert file
                file.write(f'<doc source="r/Slovenia" text_type="comment" author="{metadata[0]}" date="N/A" comments="N/A" votes="N/A">' + '\n')
                for i in range(0, len(row)):
                    file.write('<s>' + '\n')
                    file.write(row[i] + '\n')
                    file.write('</s>' + '\n')
                file.write('</doc>' + '\n')
