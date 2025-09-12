# GraphRAG-Evaluation-Pipeline

# Graph RAG Evaluation Pipeline

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A production-ready evaluation framework for comparing RAG (Retrieval-Augmented Generation) systems across local and global query types. This pipeline enables fair, repeatable benchmarking of vector RAG, Graph RAG, and hybrid systems with automated query synthesis and LLM-as-a-judge evaluation.

## 🚀 Features

- **Automated Query Synthesis**: Generate balanced question sets across 4 query classes (DataLocal, ActivityLocal, DataGlobal, ActivityGlobal)
- **Multi-System Support**: Evaluate vector RAG, Graph RAG, hybrid systems, and standalone implementations
- **LLM-as-a-Judge Evaluation**: Automated scoring with multiple quality dimensions (comprehensiveness, relevance, diversity, empowerment)
- **Statistical Validation**: Significance testing and A/A testing for reliable comparisons
- **Comprehensive Reporting**: Detailed analysis with visualizations and exportable results
- **Production Ready**: Configurable, scalable, and reproducible evaluation workflows

## 📊 Pipeline Overview

