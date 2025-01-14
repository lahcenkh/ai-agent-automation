# AI Agent for Network Automation

This project demonstrates an AI-powered agent that automates network operations using the `netmiko` library for network device interaction and `langchain` for building the AI agent and deepseek API. The agent can execute network commands on Cisco device : (IOS XR Always-On Sandbox) based on user queries.

## Features

- **Network Command Execution**: Execute show commands on Cisco devices using `netmiko`.
- **AI-Powered Agent**: Utilizes `langchain` and `ChatOpenAI` to interpret user queries and execute appropriate network commands.
- **Environment Variables**: Secure API keys and sensitive information using `.env` file.
- **Command-Line Interface**: Accept user queries via command-line arguments.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/ai-network-automation.git
cd ai-network-automation
```

2. **Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
- Create a .env file in the root directory.
- Add your DeepSeek API key to the .env file:
```
DEEPSEEK_API=your_deepseek_api_key_here
```
## Usage
To run the AI agent, use the following command:
```bash
python netops_ai_agent.py -q "run 'show ipv4  interface brief', and format the output to json"
```

**Output:**
```json
{
  "interfaces": [
    {
      "interface": "Loopback100",
      "ip_address": "1.1.1.100",
      "status": "Up",
      "protocol": "Up",
      "vrf_name": "default"
    },
    {
      "interface": "Loopback555",
      "ip_address": "unassigned",
      "status": "Up",
      "protocol": "Up",
      "vrf_name": "default"
    },
    {
      "interface": "MgmtEth0/RP0/CPU0/0",
      "ip_address": "10.10.20.175",
      "status": "Up",
      "protocol": "Up",
      "vrf_name": "default"
    },
    {
      "interface": "GigabitEthernet0/0/0/0",
      "ip_address": "unassigned",
      "status": "Shutdown",
      "protocol": "Down",
      "vrf_name": "default"
    },
    {
      "interface": "GigabitEthernet0/0/0/1",
      "ip_address": "unassigned",
      "status": "Shutdown",
      "protocol": "Down",
      "vrf_name": "default"
    },
    {
      "interface": "GigabitEthernet0/0/0/2",
      "ip_address": "unassigned",
      "status": "Shutdown",
      "protocol": "Down",
      "vrf_name": "default"
    },
    {
      "interface": "GigabitEthernet0/0/0/3",
      "ip_address": "unassigned",
      "status": "Shutdown",
      "protocol": "Down",
      "vrf_name": "default"
    },
    {
      "interface": "GigabitEthernet0/0/0/4",
      "ip_address": "17.17.17.17",
      "status": "Down",
      "protocol": "Down",
      "vrf_name": "default"
    },
    {
      "interface": "GigabitEthernet0/0/0/5",
      "ip_address": "unassigned",
      "status": "Shutdown",
      "protocol": "Down",
      "vrf_name": "default"
    },
    {
      "interface": "GigabitEthernet0/0/0/6",
      "ip_address": "unassigned",
      "status": "Shutdown",
      "protocol": "Down",
      "vrf_name": "default"
    }
  ]
}
```