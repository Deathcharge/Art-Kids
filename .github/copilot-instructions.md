# Art Kids Copilot Instructions

## Project Overview
Art Kids is a Streamlit web application promoting a supplemental art education program for Phenix City Schools. The app serves as a marketing and information hub for parents, schools, and partners interested in the Art Kids program.

## Architecture
- **Single-file Streamlit app** (`app.py`) with conditional page rendering
- **Navigation**: Uses horizontal button navigation with `st.columns` and `st.button` for clean top navigation with 6 pages
- **Styling**: Custom CSS embedded via `st.markdown()` with `unsafe_allow_html=True`
- **Layout**: Relies on Streamlit columns, tabs, and expanders for structure
- **No backend**: Pure frontend application with static content

## Key Components
- **Pages**: Home, About, Program Details, Why Art Matters, FAQ, Get Started
- **Dependencies**: `streamlit`, `requests` (requests unused)
- **Content**: Mix of markdown, HTML, and Streamlit components

## Development Workflow
```bash
# Install dependencies (no requirements.txt - install manually)
pip install streamlit streamlit-option-menu requests

# Run the application
streamlit run app.py

# Development: Edit app.py, refresh browser (hot reload enabled)
```

## Code Patterns
- **Navigation**: `cols = st.columns(len(options))` then `st.button()` in each column with `if st.button(): selected = option`
- **Custom styling**: `st.markdown("""<style>...</style>""", unsafe_allow_html=True)`
- **Layout**: `col1, col2 = st.columns([ratio1, ratio2])` for responsive design
- **Interactive elements**: `st.tabs()`, `st.expander()` for FAQ sections
- **Content**: `st.markdown()` with HTML for rich formatting

## File Structure
- `app.py`: Main application (533 lines)
- `assets/images/`: Static images including SVG placeholders
- `docs/`: Program documentation (README.md, curriculum, implementation guides)
- `README.md`: Project overview
- `ABOUT.md`: Detailed program information
- `CONTRIBUTING.md`: Partnership and volunteer guidelines

## Content Guidelines
- **Program focus**: Supplemental art education for grades 3-12
- **Target audience**: Parents, schools, art educators
- **Key messaging**: Bridge art education gap (55% schools lack instruction)
- **Branding**: Professional, educational, community-focused
- **Contact**: Phone 706-573-0073, email anartlesson@gmail.com

## Common Tasks
- **Add new page**: Insert new option in menu, add `elif selected == "NewPage":` block
- **Update content**: Edit markdown/HTML within page blocks
- **Modify styling**: Update CSS in the `<style>` block at top of app.py
- **Add interactive elements**: Use tabs/expanders for organized content

## Deployment
- **Platform**: Streamlit Cloud or any hosting supporting Python/Streamlit
- **No build step**: Direct deployment of app.py
- **Static assets**: None (placeholder images used)

## Quality Checks
- **Test navigation**: Ensure all menu options load correctly
- **Responsive design**: Check column layouts on different screen sizes
- **Content accuracy**: Verify program details match documentation in `docs/`
- **Styling consistency**: Maintain color scheme (primary: #2a5f7f, accent: #e07a5f)</content>
<parameter name="filePath">/workspaces/Art-Kids/.github/copilot-instructions.md