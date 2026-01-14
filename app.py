import streamlit as st
import requests
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Art Kids | Phoenix City Schools",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    :root {
        --primary: #2a5f7f;
        --accent: #e07a5f;
        --success: #4a9d6f;
        --light-bg: #f5f7fa;
    }
    
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    
    .main {
        background-color: white;
    }
    
    .stMetric {
        background-color: var(--light-bg);
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid var(--accent);
    }
    
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #2a5f7f;
        margin: 1.5rem 0 1rem 0;
        line-height: 1.2;
    }
    
    .section-title {
        font-size: 2.2rem;
        color: #2a5f7f;
        font-weight: 700;
        margin: 2rem 0 1.5rem 0;
        border-bottom: 3px solid #e07a5f;
        padding-bottom: 0.5rem;
        clear: both;
    }
    
    .benefit-box {
        background: linear-gradient(135deg, #2a5f7f 0%, #4a8fbf 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    
    .benefit-box h4 {
        margin: 0 0 0.5rem 0;
        color: white;
        font-size: 1.1rem;
    }
    
    .benefit-box p {
        margin: 0;
        color: rgba(255,255,255,0.9);
        line-height: 1.4;
        font-size: 0.95rem;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #2a5f7f 0%, #4a8fbf 100%);
        color: white;
        padding: 2rem;
        border-radius: 8px;
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    .cta-button {
        display: inline-block;
        background-color: #2a5f7f;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        margin: 0.5rem 0.5rem 0.5rem 0;
        transition: all 0.3s ease;
        border: 2px solid #2a5f7f;
    }
    
    .cta-button:hover {
        background-color: #1e4a5f;
        border-color: #1e4a5f;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(42, 95, 127, 0.3);
    }
    
    /* Responsive design fixes */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.2rem;
            margin: 1rem 0 0.5rem 0;
        }
        
        .section-title {
            font-size: 1.8rem;
            margin: 1.5rem 0 1rem 0;
        }
        
        .benefit-box {
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .stat-card {
            padding: 1.5rem;
        }
        
        .stat-number {
            font-size: 2rem;
        }
    }
    
    /* Prevent text overlap */
    .stMarkdown {
        overflow-wrap: break-word;
        word-wrap: break-word;
    }
    
    /* Ensure proper spacing in columns */
    .element-container {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Navigation using horizontal button bar
st.markdown("""
<style>
    .nav-container {
        background: linear-gradient(135deg, #2a5f7f 0%, #4a8fbf 100%);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .nav-buttons {
        display: flex;
        gap: 0.5rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    .nav-button {
        background: rgba(255,255,255,0.1);
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
        padding: 0.5rem 1rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 0.9rem;
    }
    .nav-button:hover {
        background: rgba(255,255,255,0.2);
        transform: translateY(-1px);
    }
    .nav-button.active {
        background: #e07a5f;
        border-color: #e07a5f;
    }
    @media (max-width: 768px) {
        .nav-buttons {
            gap: 0.25rem;
        }
        .nav-button {
            padding: 0.4rem 0.8rem;
            font-size: 0.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Create horizontal navigation using columns
nav_options = ["🏠 Home", "ℹ️ About", "📚 Program Details", "💡 Why Art Matters", "❓ FAQ", "🚀 Get Started"]
cols = st.columns(len(nav_options))

selected = None
for i, option in enumerate(nav_options):
    with cols[i]:
        if st.button(option, key=f"nav_{i}", use_container_width=True):
            selected = option.split(" ", 1)[1]  # Remove emoji, keep text

# Default to Home if no button clicked
if selected is None:
    selected = st.session_state.get('current_page', 'Home')
else:
    st.session_state.current_page = selected

# ============ HOME PAGE ============
if selected == "Home":
    st.markdown('<h1 class="hero-title">🎨 Art Kids</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #666; font-size: 1.5rem; margin: 0.5rem 0 2rem 0; line-height: 1.3;">Advancing Arts Education in Phoenix City Schools</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("""
        ### Unlocking Artistic Excellence
        
        Art Kids is a supplemental art program designed to provide talented and interested students 
        with advanced instruction in multiple mediums and techniques.
        
        **Our Mission:** Every student in Phoenix City deserves access to quality art education, 
        regardless of their school's funding.
        """)
        
        st.markdown("""
        #### Why Now?
        - **55%** of Alabama schools provide little to no art instruction
        - **93%** of lowest-performing schools lack art access
        - **90%** of highest-performing schools have strong art programs
        
        The gap is real. Art Kids is here to bridge it.
        """)
        
        st.markdown("""
        <div style="display: flex; gap: 1rem; margin: 2rem 0;">
            <a href="tel:7065730073" class="cta-button">📞 Call: 706-573-0073</a>
            <a href="mailto:anartlesson@gmail.com" class="cta-button">📧 Email Us</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Pitch Deck Section
        st.markdown("---")
        st.markdown("### 📊 Program Presentation")
        st.markdown("Download our comprehensive pitch deck to learn more about the Art Kids program:")
        
        col_preview, col_download = st.columns(2)
        
        with col_preview:
            if st.button("👁️ Preview Pitch Deck", use_container_width=True):
                st.markdown("""
                <div style="border: 2px solid #e07a5f; border-radius: 8px; padding: 1rem; margin: 1rem 0; background: #f9f9f9;">
                    <h4 style="color: #2a5f7f; margin: 0 0 0.5rem 0;">📋 Art Kids Pitch Deck</h4>
                    <p style="margin: 0; font-size: 0.9rem; color: #666;">
                        Our professional presentation covers the art education gap, program benefits, 
                        implementation details, and success metrics. Perfect for schools, partners, and stakeholders.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                st.info("💡 **Tip:** Download the pitch deck below to view the full presentation offline, or open it in your browser after downloading.")
        
        with col_download:
            # Create download button for pitch deck
            with open("pitch-deck.html", "r", encoding="utf-8") as f:
                pitch_deck_content = f.read()
            
            st.download_button(
                label="📥 Download Pitch Deck",
                data=pitch_deck_content,
                file_name="Art_Kids_Pitch_Deck.html",
                mime="text/html",
                use_container_width=True
            )
            st.markdown("*Download and open in your browser to view the full presentation*")
    
    with col2:
        st.image("assets/images/art-kids-placeholder.svg", use_column_width=True)

# ============ ABOUT PAGE ============
elif selected == "About":
    st.markdown('<h2 class="section-title">About Art Kids</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Our Story
        
        Art Kids was founded on the belief that every student should have access to quality 
        art instruction, regardless of their school's budget constraints.
        
        **Our founder** has years of experience teaching visual arts and has guided students 
        to **state and national award wins**. Now, we're bringing that same excellence to 
        Phoenix City schools.
        """)
        
        st.markdown("""
        ### What Makes Us Different
        - ✓ **Proven Track Record**: Award-winning students from Columbus studio
        - ✓ **Advanced Instruction**: Multiple mediums + cutting-edge techniques
        - ✓ **Flexible Format**: Classes at YOUR school as a fundraiser
        - ✓ **Parent-Friendly Pricing**: Comparable to Drama Kids program
        """)
    
    with col2:
        st.markdown("""
        ### The Art Kids Difference
        """)
        
        comparison_data = {
            "Feature": ["Teacher Experience", "Student Results", "Funding", "Flexibility", "Community Benefit"],
            "Art Kids": ["Award-winning", "State/National competition ready", "Parent-funded", "Multiple schools", "Fundraiser for schools"],
            "Traditional Classes": ["Varied", "Grade-level focused", "School-dependent", "One location", "No additional benefit"]
        }
        
        st.table(comparison_data)

# ============ PROGRAM DETAILS PAGE ============
elif selected == "Program Details":
    st.markdown('<h2 class="section-title">Program Details</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("""
        ### Program Structure
        """)
        
        tabs = st.tabs(["Schedule", "Mediums", "Cost", "Requirements"])
        
        with tabs[0]:
            st.markdown("""
            **Weekly Classes**
            - 📅 Every week (school year schedule)
            - ⏰ 3:30 PM – 4:30 PM (1 hour)
            - 📍 Held at partner schools throughout Phoenix City
            
            Classes rotate to different schools to benefit the community.
            """)
        
        with tabs[1]:
            st.markdown("""
            **Art Mediums & Techniques**
            
            Our curriculum exposes students to:
            - 🎨 Drawing & Sketching (foundational skills)
            - 🖼️ Painting (acrylics, oils, watercolor)
            - 🏺 Ceramics & Sculpture
            - 🖨️ Printmaking & Design
            - 📸 Digital & Mixed Media
            - 🎭 Conceptual & Fine Art
            
            Plus advanced techniques in perspective, color theory, composition, and more.
            """)
        
        with tabs[2]:
            st.markdown("""
            **Pricing**
            
            Art Kids is **parent-funded** and **comparable to Drama Kids rates**.
            
            ✓ Accessible pricing for families
            ✓ Flexible payment options available
            ✓ Financial assistance may be available—ask us!
            
            A percentage of every enrollment is donated back to the host school.
            """)
        
        with tabs[3]:
            st.markdown("""
            **Who Should Apply?**
            
            Art Kids is designed for students who:
            - ✓ Show genuine interest in visual arts
            - ✓ Demonstrate artistic talent
            - ✓ Are grades 3–12
            - ✓ Want advanced instruction beyond school curriculum
            - ✓ Are ready to develop their skills seriously
            
            This is not a recreation class—it's serious artistic development.
            """)
    
    with col2:
        st.markdown("### Quick Stats")
        
        col_stats1, col_stats2 = st.columns(2)
        with col_stats1:
            st.markdown("""
            <div class="stat-card">
                <div class="stat-number">55%</div>
                <div class="stat-label">Schools Lack Art Instruction</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_stats2:
            st.markdown("""
            <div class="stat-card">
                <div class="stat-number">90%</div>
                <div class="stat-label">Top Schools Have Art Access</div>
            </div>
            """, unsafe_allow_html=True)

# ============ WHY ART MATTERS PAGE ============
elif selected == "Why Art Matters":
    st.markdown('<h2 class="section-title">Why Art Education Matters</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    Art is far more than aesthetics—it's a crucial component of comprehensive education that develops 
    core academic and life skills.
    """)
    
    col1, col2 = st.columns(2)
    
    benefits = [
        ("👁️ Hand-Eye Coordination", "Develops fine motor control essential for writing, typing, and precision tasks"),
        ("🧠 Spatial Recognition", "Critical thinking skill required for math, science, engineering, and navigation"),
        ("🔧 Problem-Solving Skills", "Art teaches creative approaches to complex challenges"),
        ("🎯 Decision Making", "Students learn to make intentional creative choices and defend them"),
        ("🧩 Critical Thinking", "Analysis, evaluation, and synthesis of visual information"),
        ("💬 Accepting Criticism", "Builds resilience through constructive feedback and iteration")
    ]
    
    for i, (title, desc) in enumerate(benefits):
        if i % 2 == 0:
            col = col1
        else:
            col = col2
        
        with col:
            st.markdown(f"""
            <div class="benefit-box">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### The Research Says It All
    
    According to educational research:
    - Students with high arts engagement score **10-15% higher** on standardized tests
    - Art programs improve **attendance rates** and **graduation rates**
    - Arts education supports **social-emotional development**
    - Visual art study strengthens **STEM skills** through spatial reasoning
    
    **The Data Gap:** Despite the research, 55% of Alabama schools provide little to no art instruction, 
    while 90% of top-performing schools prioritize arts access.
    """)

# ============ FAQ PAGE ============
elif selected == "FAQ":
    st.markdown('<h2 class="section-title">Frequently Asked Questions</h2>', unsafe_allow_html=True)
    
    with st.expander("Is Art Kids similar to Drama Kids?", expanded=True):
        st.markdown("""
        Yes! Art Kids follows the proven Drama Kids model of supplemental arts instruction. 
        Like Drama Kids, we:
        - Are parent-funded
        - Meet weekly after school
        - Focus on serious skill development
        - Help students compete at state/national levels
        - Support the host school through fundraising
        """)
    
    with st.expander("How much does it cost?"):
        st.markdown("""
        Art Kids pricing is **comparable to Drama Kids rates**. 
        
        We believe quality arts education should be accessible. Financial assistance may be available 
        for families who need it—please ask us directly!
        """)
    
    with st.expander("What if my child is a beginner?"):
        st.markdown("""
        Art Kids accepts students at various skill levels, but our focus is on **advanced instruction 
        and serious artistic development**. 
        
        If your student is interested but hasn't taken art before, they should demonstrate:
        - Genuine interest in visual arts
        - Willingness to develop skills seriously
        - Ability to commit to weekly classes
        
        Contact us to discuss your student's background!
        """)
    
    with st.expander("Which schools host Art Kids?"):
        st.markdown("""
        Art Kids classes rotate to different schools throughout Phoenix City to serve the community. 
        We're currently establishing partnerships with interested schools.
        
        **If your school is interested in hosting Art Kids:**
        - Classes are held at your campus
        - A percentage of fees are donated back to your school
        - It's a win-win for your community!
        """)
    
    with st.expander("How do students compete in state/national competitions?"):
        st.markdown("""
        Through Art Kids instruction, students prepare high-quality artwork and enter regional, state, 
        and national art competitions. Our founder has a track record of students winning:
        - 🏆 State art awards
        - 🏆 National art competition placement
        
        We'll guide students through the competition process and help them prepare competitive pieces.
        """)
    
    with st.expander("What grades does Art Kids serve?"):
        st.markdown("""
        Art Kids currently serves students in **grades 3–12**. 
        
        We may expand to younger grades depending on demand and teacher availability.
        """)
    
    with st.expander("How do I sign my student up?"):
        st.markdown("""
        Great question! **Enrollment process:**
        
        1. 📞 **Call us**: 706-573-0073
        2. 📧 **Email**: anartlesson@gmail.com
        3. 📝 **Tell us**: About your student's art interest & experience
        4. 🤝 **Schedule a meeting**: Discuss which class location works best
        5. ✅ **Enroll**: Complete registration and payment
        
        We'll help match your student with the right class schedule and location!
        """)

# ============ GET STARTED PAGE ============
elif selected == "Get Started":
    st.markdown('<h2 class="section-title">Get Started with Art Kids</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("""
        ### Ready to Join Art Kids?
        
        It's easy to get started. Just reach out to us!
        """)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2a5f7f 0%, #4a8fbf 100%); color: white; padding: 2rem; border-radius: 8px; margin: 1.5rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h4 style="color: white; margin: 0 0 0.5rem 0; font-size: 1.1rem;">📞 Call Us</h4>
            <p style="font-size: 1.2rem; margin: 0; font-weight: 600;">706-573-0073</p>
            <p style="color: rgba(255,255,255,0.9); margin-top: 0.5rem; font-size: 0.95rem;">Ask about current class locations and schedule</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2a5f7f 0%, #4a8fbf 100%); color: white; padding: 2rem; border-radius: 8px; margin: 1.5rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h4 style="color: white; margin: 0 0 0.5rem 0; font-size: 1.1rem;">📧 Email Us</h4>
            <p style="font-size: 1.1rem; margin: 0; font-weight: 600;">anartlesson@gmail.com</p>
            <p style="color: rgba(255,255,255,0.9); margin-top: 0.5rem; font-size: 0.95rem;">Tell us about your student and we'll respond within 24 hours</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### What to Expect")
        
        st.markdown("""
        **Step 1: Initial Contact**
        - Call or email us with basic info about your student
        - We'll answer any questions you have
        
        **Step 2: Meet & Discuss**
        - Brief conversation about your student's interests & goals
        - Learn about available class locations and times
        
        **Step 3: Enroll**
        - Register your student
        - Complete parent/guardian consent forms
        - Arrange payment
        
        **Step 4: First Class!**
        - Your student attends their first Art Kids class
        - They'll be ready to start developing their artistic skills
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Why Families Choose Art Kids
    
    ✓ **Serious Instruction** – Not recreational, but skill development  
    ✓ **Proven Results** – Our students win competitions  
    ✓ **Experienced Teaching** – Award-winning instructor  
    ✓ **Accessible Format** – Classes at schools near you  
    ✓ **Community Benefit** – Your school fundraises too  
    ✓ **Flexible Options** – Multiple class locations available  
    """)
    
    st.markdown("""
    ### Parent Testimonial Placeholder
    
    > "Art Kids gave my daughter the opportunity to develop skills she never would have had access to 
    > through her school. She's more confident, more creative, and genuinely excited about art."
    > — *Phoenix City Parent*
    """)

# ============ FOOTER ============
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666; font-size: 0.9rem;">
    <p><strong>Art Kids</strong> | Advancing Arts Education in Phoenix City Schools</p>
    <p>📞 706-573-0073 | 📧 anartlesson@gmail.com</p>
    <p style="margin-top: 1rem;">© 2026 Art Kids. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)