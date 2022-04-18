# Preface

Whether it's realized or not, most people are log(wealth) maximalists, contrary to maximizing linear wealth. What does this mean? Effectively, we *dislike* the risk of loss more than we *like* potential for gain, increasingly so at the progressive ends of each.

For example:

Let's say you have a net worth of $20k. Now, it's your lucky day; you are presented with a +EV bet.
Someone offers to flip a coin. If it lands on heads, you give them $10k. If it lands on tails, they give you $12k.

You have 50/50 odds with an assymetric risk:reward bet in your favor. You should take your chances, right? Probably not.

A linear wealth maximalist would accept this bet, while a log wealth maximalist would reject it. For the latter, risk:reward is assessed logarithmically.

In the scenario of heads, your NW multiplier is .5 ((20k-10k)/20k)).
In the scenario of tails, your NW multiplier is 1.6 ((20k+12k)/20k)).

So, you can then take the natural log of both of these values. ln(.5) = -.69 ; ln(1.6) = .47

For a log wealth maximalist, only now can you take these values and assess linearly.

You have 50/50 odds with a win value of .47 and a lose value of -.69. Is this a bet you should take? No, it has a negative log expected value.


# Okay, so why does this matter? 

The concept of log wealth maximization sets the stage for an existing problem within the investment domain of which there are not practical solutions for, especially for retail investors.

Most people realize that it's a good idea to hold exposure in assets with expected *growth*, like equities and real estate. However, most people are also cautious about limiting their exposure, because they are intuitive log wealth maximalists, even if they don't explicity realize it. 

So, how might one go about maintaining the maximum about of exposure in growth assets while holding assymetric averseness to downside risk? Well, the easiest and most common way to do this is simply limiting the amount invested, and keeping the rest in low risk credit markets or even USD.

But is there a more effective way of doing this? Yes, by using a cool instrument that is traditionally known as an options contract.

# So what is the problem?

The barrier of entry for correctly using options contracts as an effective hedging tool is high. As of now, the most common use of options contracts for retail investors is high leverage gambling.

# Then what is the solution?

My proposition to build a market platform with a completely different way of framing options contracts. Currently, options are bought and sold on an esoteric-looking grid of varying expiration dates, strike prices, and type, ie. call or put. If we refer to the number of expiry choices as D and the number of strike price choices as S, we can say that there are 2 * D * S different markets within one options orderbook. If an options orderbook has 15 choices for expiry dates and each 10 strike price choices, that is 2 * (15) * (10) = ***300*** distinct markets for one orderbook.

*How in the world is the typical retail investor expected to navigate this properly?*

My proposed solution is to condense traditional options into a simple, intuitive interface that supports the most useful actual hedging mechanism that they can represent, ***insurance***. More specifically, ***investors insurance***.

# What would this look like?

Let's look at how insurance works in other markets, for example, a simplified version of home insurance.

You own a home with some market value. You want (or are required, but let's ignore that) protection in the event of a black swan event like a hurricane. Otherwise, you face the risk financial ruin if something destroys your home.

So you request a quote from an insurance company. Assuming you default to replacement cost coverage, you only have one main decision:

How high of a deductible do you opt for? You know the deductible is inversely determinant of your premiums, so you want to go as high as you can, up to the point at which the out of pocket cost of the deductible would begin affecting your financial wellbeing at an *increasingly* negative rate.


So let's transpose how this concept of *insurance* can be applied to investments.

Reverting to the first example, you have a net worth of $20k. You want as much possible exposure to growth investments but also determine that if your portfolio drops below a certain threshold, let's say $5k, cumulative losses below that will affect your wellbeing at an *increasingly* negative rate.

So what you have done here is figured out your optimal investment insurance deductible; $15k (20k-5k).

With traditional options, you could purchase a *synthetic* insurance policy on your portfolio by purchasing x put option contracts at y strike price on an indefinite cycle of expiries. If we pretend your portfolio holds only one asset and 1 contract = 1 unit, x is (((D*(1+(P/U))/U)) where V is the portfolio value, D is the optimal deductible, P is the premium at given strike price and U is the underlying spot price of the asset. y is ((C/V)*U)) where C is the point of inflection on your wellbeing function.

Point being, the only two variable inputs of an investor needed to determine the optimal hedging contract (policy) is (1) Portfolio contents and (2) Optimal deductible ie. point of inflection on wellbeing curve as a function of net worth.


























Let's say you like Bitcoin. You think the valuation will increase..a lot. So you want to put all your money, let's say $50k, into Bitcoin.

You have one problem though, you realize it's still *possible* that things could go south, and you don't want be in financial ruins if this happens. So you determine a net worth threshhold at which your quality of life begins decreasing rapidly, let's say $20k. Technically we could call this a point of inflection on your satisfaction (utility) curve as a function of net worth.

So how do you approach this situation? You want as much exposure to Bitcoin as possible, while maintaining increasingly minimal risk below $20k net worth.
Well, the easiest solution is to put $30k into Bitcoin and leave the other $20k in USD. Problem solved, right? Well, there's an even better solution.

First, it's important to remember how efficient markets function. Market forces are an aggregate of many individuals and entities. Therefore, efficient markets don't have arbitrary asset price points at which the supply and demand relationship changes it's velocity.

Why is this important? Your optimal curve in respect to the risk | reward function of an asset is **different** from the market's optimal curve.
This means that the aggregate *satisfaction* or *dissatisfaction* of market events is non-zero-sum. Unlike alpha, which is inherently zero-sum.

So, all this is to say that the difference in your satisfaction curve as a function of asset price in contrast to the market's aggregate satisfaction curve means that this is something each entity/individual in the world can theoretically optimize with no competitive forces.


This fundamental concept is why insurance ***can*** be a transaction of mutualism. In most insurance domains, options of coverage are limited to a discrete list of intuitive choices for the buyer. However, the closest instruments for constructing the optimal *insurance policy* for your investment portfolio are options contracts; and options contracts are much more difficult to effectively intuit than traditional insurance, meaning they are rarely used as an effective hedge around their personal satisfaction curve.

What is a solution to this problem? Simplifying options contracts into a more digestable and intuitive interface for investors.

