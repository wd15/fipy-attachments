<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  
  

  
    



    <head>
    <title>
      matplotlibbug.py on Ticket #114 – Attachment
     – FiPy
    </title>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!--[if IE]><script type="text/javascript">
      if (/^#__msie303:/.test(window.location.hash))
        window.location.replace(window.location.hash.replace(/^#__msie303:/, '#'));
    </script><![endif]-->
        <link rel="search" href="/fipy/search" />
        <link rel="help" href="/fipy/wiki/TracGuide" />
        <link rel="alternate" href="/fipy/raw-attachment/ticket/114/matplotlibbug.py" type="application/x-python; charset=iso-8859-15" title="Original Format" />
        <link rel="up" href="/fipy/ticket/114" title="Ticket #114" />
        <link rel="start" href="/fipy/wiki" />
        <link rel="stylesheet" href="/trac_1.0_htdocs/css/trac.css" type="text/css" /><link rel="stylesheet" href="/fipy/pygments/trac.css" type="text/css" /><link rel="stylesheet" href="/trac_1.0_htdocs/css/code.css" type="text/css" />
        <link rel="shortcut icon" href="/fipy/chrome/common/trac.ico" type="image/x-icon" />
        <link rel="icon" href="/fipy/chrome/common/trac.ico" type="image/x-icon" />
      <link type="application/opensearchdescription+xml" rel="search" href="/fipy/search/opensearch" title="Search FiPy" />
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/jquery.js"></script>
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/babel.js"></script>
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/trac.js"></script>
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/search.js"></script>
      <script type="text/javascript" src="/trac_1.0_htdocs/js/folding.js"></script>
      <script type="text/javascript">
        jQuery(document).ready(function($) {
          $('#preview table.code').enableCollapsibleColumns($('#preview table.code thead th.content'));
        });
      </script>
        <link rel="stylesheet" type="text/css" href="/trac_1.0_htdocs//css/matdlosi.css" />
	<style type="text/css">
	body {width: 95%;}
	</style>
    </head>
    <body>
    <div id="banner">
      <div id="header">
            <div id="topLogo">
                <img src="/trac_1.0_htdocs//hdr_main.jpg" alt="Main Header" usemap="#MatDL_Banner_Narrow_Map" />
                <map name="MatDL_Banner_Narrow_Map">
                    <area shape="rect" alt="Materials Digital Library" coords="44,53,263,70" href="http://matdl.org" />
                    <area shape="rect" alt="NSDL logo" coords="675,43,740,71" href="http://nsdl.org" />
                    <area shape="rect" alt="NSF logo" coords="686,0,731,43" href="http://nsf.gov" />
                    <area shape="rect" alt="MatDL logo" coords="44,0,158,53" href="http://matdl.org" />
                </map>
                <br />
                <br />
            </div>
            <div id="projheader">
                <h1 style="margin: 0px;">
                    <img style="width: 50px;" src="/fipy/chrome/site/fipy-logo.png" alt="FiPy" />
                FiPy: A Finite Volume PDE Solver Using Python</h1>
                <a href="http://www.ctcms.nist.gov/fipy">FiPy Home</a>
            </div>
        </div>
      <form id="search" action="/fipy/search" method="get">
        <div>
          <label for="proj-search">Search:</label>
          <input type="text" id="proj-search" name="q" size="18" value="" />
          <input type="submit" value="Search" />
        </div>
      </form>
      <div id="metanav" class="nav">
    <ul>
      <li class="first"><a href="/fipy/login">Login</a></li><li><a href="/fipy/wiki/TracGuide">Help/Guide</a></li><li><a href="/fipy/about">About Trac</a></li><li><a href="http://matforge.org">Matforge Home</a></li><li><a href="/fipy/register">Register</a></li><li><a href="http://matforge.org/participate.html">Participate</a></li><li class="last"><a href="/fipy/prefs">Preferences</a></li>
    </ul>
  </div>
    </div>
    <div id="mainnav" class="nav">
    <ul>
      <li class="first"><a href="/fipy/wiki">Wiki</a></li><li><a href="/fipy/blog">Blog</a></li><li><a href="/fipy/timeline">Timeline</a></li><li><a href="/fipy/roadmap">Roadmap</a></li><li><a href="/fipy/browser">Browse Source</a></li><li><a href="/fipy/report">View Tickets</a></li><li><a href="http://build.cmi.kent.edu:8010/waterfall">Buildbot</a></li><li class="last"><a href="http://build.cmi.kent.edu/codespeed">Codespeed</a></li>
    </ul>
  </div>
    <div id="main">
      <div id="ctxtnav" class="nav">
        <h2>Context Navigation</h2>
        <ul>
          <li class="last first"><a href="/fipy/ticket/114">Back to Ticket #114</a></li>
        </ul>
        <hr />
      </div>
    <div id="content" class="attachment">
        <h1><a href="/fipy/ticket/114">Ticket #114</a>: matplotlibbug.py</h1>
        <table id="info" summary="Description">
          <tbody>
            <tr>
              <th scope="col">File matplotlibbug.py,
                <span title="711 bytes">711 bytes</span>
                (added by wd15, <a class="timeline" href="/fipy/timeline?from=2007-02-09T17%3A24%3A31-05%3A00&amp;precision=second" title="See timeline at 02/09/07 17:24:31">8 years ago</a>)</th>
            </tr>
            <tr>
              <td class="message searchable">
                
              </td>
            </tr>
          </tbody>
        </table>
        <div id="preview" class="searchable">
          
  <table class="code"><thead><tr><th class="lineno" title="Line numbers">Line</th><th class="content"> </th></tr></thead><tbody><tr><th id="L1"><a href="#L1">1</a></th><td><span class="kn">import</span> <span class="nn">pylab</span><span class="o">,</span> <span class="nn">numpy</span></td></tr><tr><th id="L2"><a href="#L2">2</a></th><td></td></tr><tr><th id="L3"><a href="#L3">3</a></th><td>pylab<span class="o">.</span>ion<span class="p">()</span></td></tr><tr><th id="L4"><a href="#L4">4</a></th><td></td></tr><tr><th id="L5"><a href="#L5">5</a></th><td>data0 <span class="o">=</span> numpy<span class="o">.</span>zeros<span class="p">((</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span> <span class="s">'d'</span><span class="p">)</span></td></tr><tr><th id="L6"><a href="#L6">6</a></th><td>data1 <span class="o">=</span> numpy<span class="o">.</span>zeros<span class="p">((</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span> <span class="s">'d'</span><span class="p">)</span></td></tr><tr><th id="L7"><a href="#L7">7</a></th><td></td></tr><tr><th id="L8"><a href="#L8">8</a></th><td><span class="c">## make figure 0</span></td></tr><tr><th id="L9"><a href="#L9">9</a></th><td></td></tr><tr><th id="L10"><a href="#L10">10</a></th><td>fig0 <span class="o">=</span> pylab<span class="o">.</span>figure<span class="p">()</span></td></tr><tr><th id="L11"><a href="#L11">11</a></th><td>pylab<span class="o">.</span>title<span class="p">(</span><span class="s">'data0'</span><span class="p">)</span></td></tr><tr><th id="L12"><a href="#L12">12</a></th><td>image0 <span class="o">=</span> pylab<span class="o">.</span>imshow<span class="p">(</span>data0<span class="p">)</span></td></tr><tr><th id="L13"><a href="#L13">13</a></th><td>pylab<span class="o">.</span>colorbar<span class="p">()</span></td></tr><tr><th id="L14"><a href="#L14">14</a></th><td>pylab<span class="o">.</span>draw<span class="p">()</span></td></tr><tr><th id="L15"><a href="#L15">15</a></th><td><span class="nb">raw_input</span><span class="p">(</span><span class="s">'fig 0'</span><span class="p">)</span></td></tr><tr><th id="L16"><a href="#L16">16</a></th><td></td></tr><tr><th id="L17"><a href="#L17">17</a></th><td><span class="c">## make figure 1</span></td></tr><tr><th id="L18"><a href="#L18">18</a></th><td></td></tr><tr><th id="L19"><a href="#L19">19</a></th><td>fig1 <span class="o">=</span> pylab<span class="o">.</span>figure<span class="p">()</span></td></tr><tr><th id="L20"><a href="#L20">20</a></th><td>pylab<span class="o">.</span>title<span class="p">(</span><span class="s">'data1'</span><span class="p">)</span></td></tr><tr><th id="L21"><a href="#L21">21</a></th><td>image1 <span class="o">=</span> pylab<span class="o">.</span>imshow<span class="p">(</span>data1<span class="p">)</span></td></tr><tr><th id="L22"><a href="#L22">22</a></th><td>pylab<span class="o">.</span>colorbar<span class="p">()</span></td></tr><tr><th id="L23"><a href="#L23">23</a></th><td>pylab<span class="o">.</span>draw<span class="p">()</span></td></tr><tr><th id="L24"><a href="#L24">24</a></th><td><span class="nb">raw_input</span><span class="p">(</span><span class="s">'fig 1'</span><span class="p">)</span></td></tr><tr><th id="L25"><a href="#L25">25</a></th><td></td></tr><tr><th id="L26"><a href="#L26">26</a></th><td><span class="c">## redraw figure 0 with new data</span></td></tr><tr><th id="L27"><a href="#L27">27</a></th><td></td></tr><tr><th id="L28"><a href="#L28">28</a></th><td>newdata <span class="o">=</span> numpy<span class="o">.</span>array<span class="p">(((</span><span class="mf">0.</span><span class="p">,</span><span class="mf">1.</span><span class="p">),(</span><span class="mf">2.</span><span class="p">,</span><span class="mf">3.</span><span class="p">)))</span></td></tr><tr><th id="L29"><a href="#L29">29</a></th><td>pylab<span class="o">.</span>figure<span class="p">(</span>fig0<span class="o">.</span>number<span class="p">)</span></td></tr><tr><th id="L30"><a href="#L30">30</a></th><td>image0<span class="o">.</span>set_data<span class="p">(</span>newdata<span class="p">)</span></td></tr><tr><th id="L31"><a href="#L31">31</a></th><td><span class="c">##pylab.clim(vmax=3, vmin=0)</span></td></tr><tr><th id="L32"><a href="#L32">32</a></th><td>pylab<span class="o">.</span>draw<span class="p">()</span></td></tr><tr><th id="L33"><a href="#L33">33</a></th><td><span class="nb">raw_input</span><span class="p">(</span><span class="s">'fig 0'</span><span class="p">)</span></td></tr><tr><th id="L34"><a href="#L34">34</a></th><td></td></tr><tr><th id="L35"><a href="#L35">35</a></th><td><span class="c">## redraw figure 1 with new data</span></td></tr><tr><th id="L36"><a href="#L36">36</a></th><td></td></tr><tr><th id="L37"><a href="#L37">37</a></th><td>pylab<span class="o">.</span>figure<span class="p">(</span>fig1<span class="o">.</span>number<span class="p">)</span></td></tr><tr><th id="L38"><a href="#L38">38</a></th><td>image1<span class="o">.</span>set_data<span class="p">(</span>newdata<span class="p">)</span></td></tr><tr><th id="L39"><a href="#L39">39</a></th><td>pylab<span class="o">.</span>clim<span class="p">(</span>vmax<span class="o">=</span><span class="mi">3</span><span class="p">,</span> vmin<span class="o">=</span><span class="mi">0</span><span class="p">)</span></td></tr><tr><th id="L40"><a href="#L40">40</a></th><td>pylab<span class="o">.</span>draw<span class="p">()</span></td></tr><tr><th id="L41"><a href="#L41">41</a></th><td><span class="nb">raw_input</span><span class="p">(</span><span class="s">'fig 1'</span><span class="p">)</span></td></tr></tbody></table>

        </div>
    </div>
    <div id="altlinks">
      <h3>Download in other formats:</h3>
      <ul>
        <li class="last first">
          <a rel="nofollow" href="/fipy/raw-attachment/ticket/114/matplotlibbug.py">Original Format</a>
        </li>
      </ul>
    </div>
    </div>
    <div id="footer" lang="en" xml:lang="en">
            <div id="projfooter"><!-- Project specific footer start -->
                <script type="text/javascript"> if (window.runOnloadHook) runOnloadHook();</script>
                <script type="text/javascript">
                    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
                    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
                </script>
                <script type="text/javascript">
                    var pageTracker = _gat._getTracker("UA-2981268-9");
                    pageTracker._initData();
                    pageTracker._trackPageview();
                </script>
            </div><!-- Project specific footer end -->
            <div id="footer_banner">
                <img src="/trac_1.0_htdocs//footer.gif" width="840" height="45" border="0" usemap="#footer" />
                <map name="footer" id="footer">
                    <area shape="rect" coords="2,3,133,42" href="http://www.kent.edu" target="_blank" alt="Kent State University" />
                    <area shape="rect" coords="137,3,240,41" href="http://www.nist.gov" target="_blank" alt="NIST" />
                    <area shape="rect" coords="244,3,372,39" href="http://www.mit.edu" target="_blank" alt="MIT" />
                    <area shape="rect" coords="376,5,606,41" href="http://www.umich.edu" target="_blank" alt="University of Michigan" />
                    <area shape="rect" coords="613,5,715,38" href="http://www.purdue.edu" target="_blank" alt="Purdue" />
                    <area shape="rect" coords="718,4,833,41" href="http://www.iastate.edu" target="_blank" alt="Iowa State University" />
                </map>
            </div>
            <br />
            <div id="altlinks">
                <br />
                <ul>
                    <li><a href="http://matdl.org/repository/about.htm" class="last first"> About </a></li>
                    <li><a href="http://matdl.org/repository/tou.htm" class="last first"> Terms of Use </a></li>
                    <li><a href="http://matdl.org/repository/contact.htm" class="last first"> Contact </a></li>
                    <li><a href="http://matdl.org/repository/priv.htm" class="last first"> Privacy Policy </a></li>
                </ul>
            </div>
	    <div id="tracfooter" lang="en" xml:lang="en">
	    <a id="tracpowered" href="http://trac.edgewall.org/"><img src="/fipy/chrome/common/trac_logo_mini.png" height="30" width="107" alt="Trac Powered" /></a>
	    <p class="left">
	    Powered by <a href="/fipy/about"><strong>Trac 1.0</strong></a><br />
	    By <a href="http://www.edgewall.org/">Edgewall Software</a>.
	    </p>
	    <p class="right">Visit the Trac open source project at<br /><a href="http://trac.edgewall.org/">http://trac.edgewall.org/</a></p>
	    </div>
        </div>
    </body>
</html>