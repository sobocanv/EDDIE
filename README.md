# Eddie

## Overview

Welcome to the Eddie repository, a linguistic corpus built from content gathered on the r/Slovenia subreddit. This corpus is tailored for NLP research, aiming to provide valuable insights into the language usage of Slovenian Reddit users.

## Table of Contents

1. [Introduction](#overview)
2. [License](#license)
3. [Contributing](#contributing)
4. [Languages](#languages)
5. [Data Sources](#data-sources)
6. [Collection Procedure](#collection-procedure)
7. [Folder Structure](#folder-structure)
8. [Usage](#usage)
9. [Acknowledgments](#acknowledgments)
10. [Contact](#contact)

## License

This corpus is licensed under the GNU General Public Licence v3.0. Please refer to the [LICENSE](LICENSE.md) file for more information.

## Contributing

Contributions are welcome to enhance the quality and coverage of this corpus. Please refer to the [CONTRIBUTING](CONTRIBUTING.md) guidelines for more information.

## Languages

The goal of this repository is to construct a representative corpus reflecting the language usage found on the r/Slovenia subreddit, a sub-forum created for and by Slovenian users of Reddit.

## Collection Procedure

### Data Source

The data was scraped from the r/Slovenia subreddit on December 5, 2023. The corpus includes around 137,637 words (218,421 tokens), making for a substantial volume of data relative to the subreddit's size (around 80,000 members) which can be considered representative.

### Methodology

Web crawling was accomplished using the Parsehub scraping software, focusing on the old Reddit site (accessible at: [http://old.reddit.com]) and filtering through the top posts from Novermber 5 to December 5, 2023.

## Folder Structure

The publicly available .vert file forming the corpus basis underwent preprocessing. Text splitting and anonymization of identifiable user data in metadata were performed using Python's regular expressions module. The CLASSLA natural processing pipeline's standard language model processed the text. The .vert file is structured with <doc> type documents, each encompassing sentences marked with <s>...</s>. Relevant metadata is included in each <doc> structure. Punctuation tokens not preceded by a space are marked with the special glue tag </g>.

## Usage

This corpus is valuable for examining linguistic anomalies and specialties within the Slovenian subculture of Reddit users. With only 0.5% of Slovenian social media users present on Reddit, r/Slovenia constitutes a linguistic bubble, providing insights into new word formations, syntax, and vocabulary within the Slovenian language.

## Acknowledgments

We express our gratitude to Mojca Brglez. Their contributions have significantly enriched the content of this corpus.

---
© 2024 University of Ljubljana, Faculty of Arts