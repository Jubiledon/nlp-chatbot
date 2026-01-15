# Interactive NLP-Based Conversational AI System

An interactive, dialogue-based NLP system designed to support users in completing transactional tasks through natural language conversation.
This project was developed in Python using classical NLP techniques, with a strong emphasis on conversational design, system architecture, and usability evaluation.

---

## Features

### Core NLP Architecture

* **Intent matching** using similarity-based and rule-based approaches
* **Text preprocessing pipeline** (tokenisation, normalisation, stopword filtering)
* **Context tracking** to support multi-turn conversations
* **Identity management** (user name detection, storage, and recall)

### Transactional Dialogue System

* Supports structured, goal-oriented interactions (e.g. booking, ordering, or management tasks)
* Slot-filling dialogue flow with validation and clarification
* Confirmation strategies to reduce user errors

### Conversational Design Principles

* Clear and structured prompts
* Discoverability via contextual guidance and help responses
* Robust error handling and recovery strategies
* Personalised responses based on user context and identity
* Explicit confirmations before completing actions

### Additional Capabilities

* Small talk handling for basic conversational grounding
* Information retrieval / question answering within the system’s domain

---

## System Architecture

The system follows a modular architecture:

```
User Input
   ↓
Text Preprocessing
   ↓
Intent Classification
   ↓
Dialogue Manager
   ├── Identity Management
   ├── Transaction Handler
   ├── Information Retrieval
   └── Small Talk Handler
   ↓
Response Generation
```

---

## Technologies Used

* **Language:** Python 3
* **Libraries (restricted set):**

  * Python Standard Library
  * NumPy
  * SciPy
  * scikit-learn
  * NLTK (excluding `nltk.chat`)
* **Paradigms:**
  Natural Language Processing, Rule-based Systems, Similarity-based Classification, Human–AI Interaction

---

## Running the System

### Prerequisites

* Python 3.x

### Run

```bash
python main.py
```

The chatbot will start in the terminal and guide the user through supported interactions.





