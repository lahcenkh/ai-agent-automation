from netmiko import ConnectHandler
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv 
from openai import OpenAI
import os
import argparse

load_dotenv(dotenv_path=".env")
DEEPSEEK_API = os.getenv('DEEPSEEK_API')

parser = argparse.ArgumentParser(description='AI Agent Network Automation')
parser.add_argument('-q', '--query', type=str, help='entre your query')
args = parser.parse_args()
USER_QUERY = args.query

def execute_network_command(command):
    device = {
        'device_type': "cisco_xr",
        'ip': "sandbox-iosxr-1.cisco.com",
        'username': "admin",
        'password': "C1sco12345",
    }
    
    try:
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_command(command)
            return output
    except Exception as e:
        return f"Error: {str(e)}"
    

network_tool = Tool(
    name="execute_network_command",
    func=execute_network_command,
    description="Use this tool to execute show commands on network devices. Input should be inculed the command argument."
)

llm = ChatOpenAI(model="deepseek-chat" ,api_key=DEEPSEEK_API, base_url="https://api.deepseek.com")


tools = [network_tool]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


response = agent.run(USER_QUERY)
print(response)