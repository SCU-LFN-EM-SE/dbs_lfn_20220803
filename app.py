{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bd0dbc28",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "759044b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3cbf11fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a1bfe933",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\", methods = [\"GET\", \"POST\"])\n",
    "\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.ger(\"rates\"))\n",
    "        print(rates)\n",
    "        \n",
    "        model1 = joblib.load(\"regression\")\n",
    "        r1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"tree\")\n",
    "        r2 = model2.predict([[rates]])\n",
    "        \n",
    "        return(render_template(\"index.html\", result1 = r1, result2 = r2))\n",
    "    \n",
    "    else:\n",
    "        return(render_template(\"index.html\", result1 = \"waiting\", result2 = \"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9eec9b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8dcab18a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78543145",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
