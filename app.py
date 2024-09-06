{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPmowtnHVTntn7QfMEMSDzg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aakifahmed2710/solar-panel-regression/blob/master/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "SCB30iQFdBpP"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import joblib\n",
        "from sklearn.preprocessing import StandardScaler"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model = joblib.load('model.pkl')\n",
        "scaler = joblib.load('scaler.pkl')"
      ],
      "metadata": {
        "id": "0IkmtfDrdbAn"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def predict_power(data):\n",
        "    # Preprocessing and scaling should be done similarly to the training phase\n",
        "    data_scaled = scaler.transform(data)  # Ensure you have saved or defined the scaler\n",
        "    prediction = model.predict(data_scaled)\n",
        "    return prediction"
      ],
      "metadata": {
        "id": "JJIzN37adrap"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    st.title(\"Solar Power Generation Prediction\")\n",
        "\n",
        "    st.sidebar.header(\"Input Parameters\")\n",
        "\n",
        "    # Define a function to capture user inputs\n",
        "    def user_input_features():\n",
        "        distance_to_solar_noon = st.sidebar.slider('Distance to Solar Noon (radians)', 0.0, 1.57, 0.78)\n",
        "        temperature = st.sidebar.slider('Temperature (°C)', -20.0, 50.0, 25.0)\n",
        "        wind_direction = st.sidebar.slider('Wind Direction (°)', 0, 360, 180)\n",
        "        wind_speed = st.sidebar.slider('Wind Speed (m/s)', 0.0, 20.0, 5.0)\n",
        "        sky_cover = st.sidebar.slider('Sky Cover (0-4)', 0, 4, 2)\n",
        "        visibility = st.sidebar.slider('Visibility (km)', 0.0, 20.0, 10.0)\n",
        "        humidity = st.sidebar.slider('Humidity (%)', 0.0, 100.0, 50.0)\n",
        "        average_wind_speed = st.sidebar.slider('Average Wind Speed (m/s)', 0.0, 20.0, 5.0)\n",
        "        average_pressure = st.sidebar.slider('Average Pressure (mercury inches)', 25.0, 35.0, 30.0)\n",
        "\n",
        "        data = {\n",
        "            'distance_to_solar_noon': distance_to_solar_noon,\n",
        "            'temperature': temperature,\n",
        "            'wind_direction': wind_direction,\n",
        "            'wind_speed': wind_speed,\n",
        "            'sky_cover': sky_cover,\n",
        "            'visibility': visibility,\n",
        "            'humidity': humidity,\n",
        "            'average_wind_speed': average_wind_speed,\n",
        "            'average_pressure': average_pressure\n",
        "        }\n",
        "        features = pd.DataFrame(data, index=[0])\n",
        "        return features\n",
        "\n",
        "    input_df = user_input_features()\n",
        "\n",
        "    st.subheader('Input Parameters')\n",
        "    st.write(input_df)\n",
        "\n",
        "    st.subheader('Predicted Solar Power Generation')\n",
        "\n",
        "    if st.button('Predict'):\n",
        "      prediction = predict_power(input_df)\n",
        "      st.write(f\"Predicted Power Generated: {prediction[0]:.2f} Joules\")\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yaqeFrsphTZo",
        "outputId": "11c0221d-aa7e-47ca-ec12-0afea346921d"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-09-06 20:38:45.193 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.196 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.199 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.203 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.205 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.207 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.210 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.211 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.212 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.214 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.217 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.219 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.221 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.222 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.224 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.226 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.228 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.229 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.231 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.232 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.234 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.235 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.237 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.238 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.242 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.243 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.245 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.247 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.248 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.250 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.252 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.254 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.255 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.256 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.258 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.259 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.261 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.268 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.279 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.283 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.310 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.312 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.322 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.324 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.326 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.328 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.330 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.331 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.333 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-09-06 20:38:45.334 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8cPuXNGkheCe"
      },
      "execution_count": 21,
      "outputs": []
    }
  ]
}