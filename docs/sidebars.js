/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

 module.exports = {
  docsSidebar: [
    'welcome',

    {
      type: 'category',
      label: 'Getting Started',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/introduction',
        'gpt-researcher/getting-started-with-docker',
        'gpt-researcher/getting-started',
        'gpt-researcher/frontend',
        'gpt-researcher/linux-deployment',
      ]
    },

    {
      type: 'category',
      label: 'GPT Researcher',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/pip-package',
        'gpt-researcher/example',
        'gpt-researcher/automated-tests',
        'gpt-researcher/troubleshooting',
      ],
    },
    
    {
      type: 'category',
      label: 'Custom Context',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/tailored-research',
        'gpt-researcher/local-docs',
        'gpt-researcher/vector-stores',
        ]
    },
    
    
    {
      type: 'category',
      label: 'Large Language Models',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/llms',
        'gpt-researcher/deploy-llm-on-elestio.md'
      ]
    },

    
    {
      type: 'category',
      label: 'More Customization',
      collapsible: true,
      collapsed: true,
      items: [
        'gpt-researcher/config',
        'gpt-researcher/retrievers',
        ]
    },
    {
      type: 'category',
      label: 'Multi-Agent Frameworks',
      collapsible: true,
      collapsed: true,
      items: [
        'gpt-researcher/langgraph',
        ]
    },
    {'Examples': [{type: 'autogenerated', dirName: 'examples'}]},
    'contribute',
  ],
  // pydoc-markdown auto-generated markdowns from docstrings
  referenceSideBar: [require("./docs/reference/sidebar.json")]
};
