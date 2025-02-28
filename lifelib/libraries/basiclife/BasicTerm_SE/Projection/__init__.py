"""The main Space in the :mod:`~basiclife.BasicTerm_SE` model.

:mod:`~basiclife.BasicTerm_SE.Projection` is the only Space defined
in the :mod:`~basiclife.BasicTerm_SE` model, and it contains
all the logic and data used in the model.

.. rubric:: Parameters and References

(In all the sample code below,
the global variable ``Projection`` refers to the
:mod:`~basiclife.BasicTerm_SE.Projection` Space.)

Attributes:

    point_id: The ID of the selected model point.
        ``point_id`` is defined as a Reference, and its value
        is used for determining the selected model point.
        By default, ``1`` is assigned. To select another model point,
        assign its model point ID to it::

            >>> Projection.point_id = 2

        ``point_id`` is also defined as the parameter of the
        :mod:`~basiclife.BasicTerm_SE.Projection` Space,
        which makes it possible to create dynamic child space
        for multiple model points::

            >>> Projection.parameters
            ('point_id',)

            >>> Projection[1]
            <ItemSpace BasicTerm_SE.Projection[1]>

            >>> Projection[2]
            <ItemSpace BasicTerm_SE.Projection[2]>

        .. seealso::

           * :attr:`model_point_table`
           * :func:`model_point`

    model_point_table: All model points as a DataFrame.
        The sample model point data was generated by
        *generate_model_points_with_duration.ipynb* included in the library.
        The DataFrame has an index named ``point_id``,
        and :func:`model_point` returns a record as a Series
        whose index value matches :attr:`point_id`.
        The DataFrame has the following columns:

            * ``age_at_entry``
            * ``sex``
            * ``policy_term``
            * ``policy_count``
            * ``sum_assured``
            * ``duration_mth``

        Cells defined in :mod:`~basiclife.BasicTerm_SE.Projection`
        with the same names as these columns return
        the corresponding column's values for the selected model point.

        .. code-block::

            >>> Projection.model_poit_table
                       age_at_entry sex  ...  sum_assured  duration_mth
            policy_id                    ...
            1                    47   M  ...       622000             1
            2                    29   M  ...       752000           210
            3                    51   F  ...       799000            15
            4                    32   F  ...       422000           125
            5                    28   M  ...       605000            55
                            ...  ..  ...          ...           ...
            9996                 47   M  ...       827000           157
            9997                 30   M  ...       826000           168
            9998                 45   F  ...       783000           146
            9999                 39   M  ...       302000            11
            10000                22   F  ...       576000           166

            [10000 rows x 6 columns]

        The DataFrame is saved in the Excel file *model_point_table.xlsx*
        placed in the model folder.
        :attr:`model_point_table` is created by
        Projection's `new_pandas`_ method,
        so that the DataFrame is saved in the separate file.
        The DataFrame has the injected attribute
        of ``_mx_dataclident``::

            >>> Projection.model_point_table._mx_dataclient
            <PandasData path='model_point_table.xlsx' filetype='excel'>

        .. seealso::

           * :attr:`point_id`
           * :func:`model_point`
           * :func:`age_at_entry`
           * :func:`sex`
           * :func:`policy_term`
           * :func:`pols_if_init`
           * :func:`sum_assured`
           * :func:`duration_mth`

    premium_table: Premium rate table by entry age and duration as a Series.
        The table is created using :mod:`~basiclife.BasicTerm_M`
        as demonstrated in *create_premium_table.ipynb*.
        The table is stored in *premium_table.xlsx* in the model folder.

        .. code-block::

            >>> Projection.premium_table
            age_at_entry  policy_term
            20            10             0.000046
                          15             0.000052
                          20             0.000057
            21            10             0.000048
                          15             0.000054
                                           ...
            58            15             0.000433
                          20             0.000557
            59            10             0.000362
                          15             0.000471
                          20             0.000609
            Name: premium_rate, Length: 120, dtype: float64

    disc_rate_ann: Annual discount rates by duration as a pandas Series.

        .. code-block::

            >>> Projection.disc_rate_ann
            year
            0      0.00000
            1      0.00555
            2      0.00684
            3      0.00788
            4      0.00866

            146    0.03025
            147    0.03033
            148    0.03041
            149    0.03049
            150    0.03056
            Name: disc_rate_ann, Length: 151, dtype: float64

        The Series is saved in the Excel file *disc_rate_ann.xlsx*
        placed in the model folder.
        :attr:`disc_rate_ann` is created by
        Projection's `new_pandas`_ method,
        so that the Series is saved in the separate file.
        The Series has the injected attribute
        of ``_mx_dataclident``::

            >>> Projection.disc_rate_ann._mx_dataclient
            <PandasData path='disc_rate_ann.xlsx' filetype='excel'>

        .. seealso::

           * :func:`disc_rate_mth`
           * :func:`disc_factors`

    mort_table: Mortality table by age and duration as a DataFrame.
        See *basic_term_sample.xlsx* included in this library
        for how the sample mortality rates are created.

        .. code-block::

            >>> Projection.mort_table
                        0         1         2         3         4         5
            Age
            18   0.000231  0.000254  0.000280  0.000308  0.000338  0.000372
            19   0.000235  0.000259  0.000285  0.000313  0.000345  0.000379
            20   0.000240  0.000264  0.000290  0.000319  0.000351  0.000386
            21   0.000245  0.000269  0.000296  0.000326  0.000359  0.000394
            22   0.000250  0.000275  0.000303  0.000333  0.000367  0.000403
            ..        ...       ...       ...       ...       ...       ...
            116  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            117  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            118  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            119  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
            120  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000

            [103 rows x 6 columns]

        The DataFrame is saved in the Excel file *mort_table.xlsx*
        placed in the model folder.
        :attr:`mort_table` is created by
        Projection's `new_pandas`_ method,
        so that the DataFrame is saved in the separate file.
        The DataFrame has the injected attribute
        of ``_mx_dataclident``::

            >>> Projection.mort_table._mx_dataclient
            <PandasData path='mort_table.xlsx' filetype='excel'>

        .. seealso::

           * :func:`mort_rate`
           * :func:`mort_rate_mth`

    np: The `numpy`_ module.
    pd: The `pandas`_ module.

.. _numpy:
   https://numpy.org/

.. _pandas:
   https://pandas.pydata.org/

.. _new_pandas:
   https://docs.modelx.io/en/latest/reference/space/generated/modelx.core.space.UserSpace.new_pandas.html

"""

from modelx.serialize.jsonvalues import *

_formula = lambda point_id: None

_bases = []

_allow_none = None

_spaces = []

# ---------------------------------------------------------------------------
# Cells

def age(t):
    """The attained age at time t.

    Defined as::

        age_at_entry() + duration(t)

    .. seealso::

        * :func:`age_at_entry`
        * :func:`duration`

    """
    return age_at_entry() + duration(t)


def age_at_entry():
    """The age at entry of the selected model point

    The element labeled ``age_at_entry`` of the Series returned by
    :func:`model_point`.
    """
    return model_point()["age_at_entry"]


def check_pv_net_cf():
    """Check present value summation

    Check if the present value of :func:`net_cf` matches the
    sum of the present values each cashflows.
    Returns the check result as :obj:`True` or :obj:`False`.

     .. seealso::

        * :func:`net_cf`
        * :func:`pv_net_cf`

    """

    import math
    res = sum(list(net_cf(t) for t in range(proj_len())) * disc_factors()[:proj_len()])

    return math.isclose(res, pv_net_cf())


def claim_pp(t):
    """Claim per policy

    The claim amount per plicy. Defaults to :func:`sum_assured`.
    """
    return sum_assured()


def claims(t):
    """Claims

    Claims during the period from ``t`` to ``t+1`` defined as::

        claim_pp(t) * pols_death(t)

    .. seealso::

        * :func:`claim_pp`
        * :func:`pols_death`

    """
    return claim_pp(t) * pols_death(t)


def commissions(t): 
    """Commissions

    By default, 100% premiums for the first year, 0 otherwise.

    .. seealso::

        * :func:`premiums`
        * :func:`duration`

    """
    return premiums(t) if duration(t) == 0 else 0


def disc_factors():
    """Discount factors.

    Vector of the discount factors as a Numpy array. Used for calculating
    the present values of cashflows.

    .. seealso::

        :func:`disc_rate_mth`
    """
    return np.array(list((1 + disc_rate_mth()[t])**(-t) for t in range(proj_len())))


def disc_rate_mth():
    """Monthly discount rate

    Nummpy array of monthly discount rates from time 0 to :func:`proj_len` - 1
    defined as::

        (1 + disc_rate_ann)**(1/12) - 1

    .. seealso::

        :func:`disc_rate_ann`

    """
    return np.array(list((1 + disc_rate_ann[t//12])**(1/12) - 1 for t in range(proj_len())))


def duration(t):
    """Duration of the selected model point at ``t`` in years

    .. seealso:: :func:`duration_mth`

    """
    return duration_mth(t) // 12


def duration_mth(t):
    """Duration of the selected model point at ``t`` in months

    Indicates how many months the policies have been in-force at ``t``.
    The initial value at time 0 is read from the ``duration_mth`` column in
    :attr:`model_point_table` through :func:`model_point`.
    Increments by 1 as ``t`` increments.
    Negative values of :func:`duration_mth` indicate future new business
    policies. For example, If the :func:`duration_mth` is
    -15 at time 0, the model point is issued at ``t=15``.

    .. seealso:: :func:`model_point`

    """
    if t == 0:
        return model_point()['duration_mth']
    else:
        return duration_mth(t-1) + 1


def expense_acq():
    """Acquisition expense per policy

    ``300`` by default.
    """
    return 300


def expense_maint():
    """Annual maintenance expense per policy

    ``60`` by default.
    """
    return 60


def expenses(t):
    """Expenses

    Expenses during the period from ``t`` to ``t+1``
    defined as the sum of acquisition expenses and maintenance expenses.
    The acquisition expenses are modeled as :func:`expense_acq`
    times :func:`pols_new_biz`.
    The maintenance expenses are modeled as :func:`expense_maint`
    times :func:`inflation_factor` times :func:`pols_if_at` before
    decrement.

    .. seealso::

        * :func:`expense_acq`
        * :func:`expense_maint`
        * :func:`inflation_factor`
        * :func:`pols_new_biz`
        * :func:`pols_if_at`

    """

    return expense_acq() * pols_new_biz(t) \
        + pols_if_at(t, "BEF_DECR") * expense_maint()/12 * inflation_factor(t)


def inflation_factor(t):
    """The inflation factor at time t

    .. seealso::

        * :func:`inflation_rate`

    """
    return (1 + inflation_rate)**(t//12)


def inflation_rate():
    """Inflation rate"""
    return 0.01


def lapse_rate(t):
    """Lapse rate

    By default, the lapse rate assumption is defined by duration as::

        max(0.1 - 0.02 * duration(t), 0.02)

    .. seealso::

        :func:`duration`

    """
    return max(0.1 - 0.02 * duration(t), 0.02)


def loading_prem():
    """Loading per premium

    .. note::
       This cells is not used by default.

    ``0.5`` by default.

    .. seealso::

        * :func:`premium_pp`

    """
    return 0.50


def model_point():
    """The selected model point as a Series

    :func:`model_point` looks up :attr:`model_point_table`, and
    returns as a Series the row whose index is the value of
    :attr:`point_id`.

    Example:
        In the code below ``Projection`` refers to
        the :mod:`~basiclife.BasicTerm_SE.Projection` space::

            >>> Projection.point_id
            1

            >>> Projection.model_point()
            age_at_entry        47
            sex                  M
            policy_term         10
            policy_count        86
            sum_assured     622000
            duration_mth         1
            Name: 1, dtype: object

            >>> Projection.point_id = 2

            >>> Projection.model_point()
            age_at_entry        29
            sex                  M
            policy_term         20
            policy_count        56
            sum_assured     752000
            duration_mth       210
            Name: 2, dtype: object

    """
    return model_point_table.loc[point_id]


def mort_rate(t):
    """Mortality rate to be applied at time t

    .. seealso::

       * :attr:`mort_table`
       * :func:`mort_rate_mth`

    """
    return mort_table[str(max(min(5, duration(t)),0))][age(t)]


def mort_rate_mth(t):
    """Monthly mortality rate to be applied at time t

    .. seealso::

       * :attr:`mort_table`
       * :func:`mort_rate`

    """
    return 1-(1- mort_rate(t))**(1/12)


def net_cf(t):
    """Net cashflow

    Net cashflow for the period from ``t`` to ``t+1`` defined as::

        premiums(t) - claims(t) - expenses(t) - commissions(t)

    .. seealso::

        * :func:`premiums`
        * :func:`claims`
        * :func:`expenses`
        * :func:`commissions`

    """
    return premiums(t) - claims(t) - expenses(t) - commissions(t)


def net_premium_pp():
    """Net premium per policy

    .. note::
       This cells is not used by default.

    The net premium per policy is defined so that
    the present value of net premiums equates to the present value of
    claims::

        pv_claims() / pv_pols_if()

    .. seealso::

        * :func:`pv_claims`
        * :func:`pv_pols_if`

    """
    return pv_claims() / pv_pols_if()


def policy_term():
    """The policy term of the selected model point.

    The element labeled ``policy_term`` of the Series returned by
    :func:`model_point`.
    """

    return model_point()["policy_term"]


def pols_death(t):
    """Number of death occurring at time t"""
    return pols_if_at(t, "BEF_DECR") * mort_rate_mth(t)


def pols_if(t):
    """Number of policies in-force

    :func:`pols_if(t)<pols_if>` is an alias
    for :func:`pols_if_at(t, "BEF_MAT")<pols_if_at>`.

    .. seealso::
        * :func:`pols_if_at`

    """
    return pols_if_at(t, "BEF_MAT")


def pols_if_at(t, timing):
    """Number of policies in-force

    :func:`pols_if_at(t, timing)<pols_if_at>` calculates
    the number of policies in-force at time ``t``.
    The second parameter ``timing`` takes a string value to
    indicate the timing of in-force,
    which is either
    ``"BEF_MAT"``, ``"BEF_NB"`` or ``"BEF_DECR"``.

    .. rubric:: BEF_MAT

    The number of policies in-force before maturity after lapse and death.
    At time 0, the value is read from :func:`pols_if_init`.
    For time > 0, defined as::

        pols_if_at(t-1, "BEF_DECR") - pols_lapse(t-1) - pols_death(t-1)

    .. rubric:: BEF_NB

    The number of policies in-force before new business after maturity.
    Defined as::

        pols_if_at(t, "BEF_MAT") - pols_maturity(t)

    .. rubric:: BEF_DECR

    The number of policies in-force before lapse and death after new business.
    Defined as::

        pols_if_at(t, "BEF_NB") + pols_new_biz(t)

    .. seealso::
        * :func:`pols_if_init`
        * :func:`pols_lapse`
        * :func:`pols_death`
        * :func:`pols_maturity`
        * :func:`pols_new_biz`
        * :func:`pols_if`

    """
    if timing == "BEF_MAT":

        if t == 0:
            return pols_if_init()
        else:
            return pols_if_at(t-1, "BEF_DECR") - pols_lapse(t-1) - pols_death(t-1)

    elif timing == "BEF_NB":

        return pols_if_at(t, "BEF_MAT") - pols_maturity(t)

    elif timing == "BEF_DECR":

        return pols_if_at(t, "BEF_NB") + pols_new_biz(t)

    else:
        raise ValueError("invalid timing")


def pols_if_init(): 
    """Initial number of policies in-force

    Number of in-force policies at time 0 referenced from
    :func:`pols_if_at(0, "BEF_MAT")<pols_if_at>`.
    """
    if duration_mth(0) > 0:
        return model_point()["policy_count"]
    else:
        return 0


def pols_lapse(t):
    """Number of lapse occurring at time t

    .. seealso::
        * :func:`pols_if_at`
        * :func:`lapse_rate`

    """
    return pols_if_at(t, "BEF_DECR") * (1-(1 - lapse_rate(t))**(1/12))


def pols_maturity(t):
    """Number of maturing policies

    The policy maturity occurs when
    :func:`duration_mth` equals 12 times :func:`policy_term`.
    The amount is equal to :func:`pols_if_at(t, "BEF_MAT")<pols_if_at>`.

    otherwise ``0``.
    """
    if duration_mth(t) == policy_term() * 12:
        return pols_if_at(t, "BEF_MAT")
    else:
        return 0


def pols_new_biz(t):
    """Number of new business policies

    The number of new business policies.
    The value :func:`duration_mth(0)<duration_mth>`
    for the selected model point is read from the ``policy_count`` column in
    :func:`model_point`. If the value is 0 or negative,
    the model point is new business at t=0 or at t when
    :func:`duration_mth(t)<duration_mth>` is 0, and the
    :func:`pols_new_biz(t)<pols_new_biz>` is read from the ``policy_count``
    in :func:`model_point`.

    .. seealso::
        * :func:`model_point`

    """
    if duration_mth(t) == 0:
        return model_point()['policy_count']
    else:
        return 0


def premium_pp():
    """Monthly premium per policy

    Monthly premium amount per policy defined as::

        round(sum_assured() * premium_table[age_at_entry(), policy_term()], 2)

    .. seealso::

        * :attr:`premium_table`
        * :func:`sum_assured`
        * :func:`age_at_entry`
        * :func:`policy_term`


    """
    return round(sum_assured() * premium_table[age_at_entry(), policy_term()], 2)


def premiums(t):
    """Premium income

    Premium income during the period from ``t`` to ``t+1`` defined as::

        premium_pp() * pols_if_at(t, "BEF_DECR")

    .. seealso::

        * :func:`premium_pp`
        * :func:`pols_if_at`

    """
    return premium_pp() * pols_if_at(t, "BEF_DECR")


def proj_len():
    """Projection length in months

    :func:`proj_len` indicates how many months the projection
    for the selected model point should be carried out. Defined as::

        12 * policy_term() - duration_mth(0) + 1

    .. seealso::

        :func:`policy_term`

    """
    return max(12 * policy_term() - duration_mth(0) + 1, 0)


def pv_claims():
    """Present value of claims

    .. seealso::

        * :func:`claims`

    """
    return sum(list(claims(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_commissions():
    """Present value of commissions

    .. seealso::

        * :func:`expenses`

    """
    return sum(list(commissions(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_expenses():
    """Present value of expenses

    .. seealso::

        * :func:`expenses`

    """
    return sum(list(expenses(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_net_cf():
    """Present value of net cashflows.

    Defined as::

        pv_premiums() - pv_claims() - pv_expenses() - pv_commissions()

    .. seealso::

        * :func:`pv_premiums`
        * :func:`pv_claims`
        * :func:`pv_expenses`
        * :func:`pv_commissions`

    """

    return pv_premiums() - pv_claims() - pv_expenses() - pv_commissions()


def pv_pols_if():
    """Present value of policies in-force

    .. note::
       This cells is not used by default.

    The discounted sum of the number of in-force policies at each month.
    It is used as the annuity factor for calculating :func:`net_premium_pp`.

    """
    return sum(list(pols_if(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def pv_premiums():
    """Present value of premiums

    .. seealso::

        * :func:`premiums`

    """
    return sum(list(premiums(t) for t in range(proj_len())) * disc_factors()[:proj_len()])


def result_cf():
    """Result table of cashflows

    .. seealso::

       * :func:`premiums`
       * :func:`claims`
       * :func:`expenses`
       * :func:`commissions`
       * :func:`net_cf`

    """

    t_len = range(proj_len())

    data = {
        "Premiums": [premiums(t) for t in t_len],
        "Claims": [claims(t) for t in t_len],
        "Expenses": [expenses(t) for t in t_len],
        "Commissions": [commissions(t) for t in t_len],
        "Net Cashflow": [net_cf(t) for t in t_len]
    }
    return pd.DataFrame.from_dict(data)


def result_pols():
    """Result table of policy decrement

    .. seealso::

       * :func:`pols_if`
       * :func:`pols_maturity`
       * :func:`pols_new_biz`
       * :func:`pols_death`
       * :func:`pols_lapse`

    """

    t_len = range(proj_len())

    data = {
        "pols_if": [pols_if(t) for t in t_len],
        "pols_maturity": [pols_maturity(t) for t in t_len],
        "pols_new_biz": [pols_new_biz(t) for t in t_len],
        "pols_death": [pols_death(t) for t in t_len],
        "pols_lapse": [pols_lapse(t) for t in t_len]
    }

    return pd.DataFrame.from_dict(data)


def result_pv():
    """Result table of present value of cashflows

    .. seealso::

       * :func:`pv_premiums`
       * :func:`pv_claims`
       * :func:`pv_expenses`
       * :func:`pv_commissions`
       * :func:`pv_net_cf`

    """

    cols = ["Premiums", "Claims", "Expenses", "Commissions", "Net Cashflow"]
    pvs = [pv_premiums(), pv_claims(), pv_expenses(), pv_commissions(), pv_net_cf()]

    return pd.DataFrame.from_dict(
            data={"PV": pvs},
            columns=cols,
            orient='index')


def sex(): 
    """The sex of the selected model point

    .. note::
       This cells is not used by default.

    The element labeled ``sex`` of the Series returned by
    :func:`model_point`.
    """
    return model_point()["sex"]


def sum_assured():
    """The sum assured of the selected model point

    The element labeled ``sum_assured`` of the Series returned by
    :func:`model_point`.
    """
    return model_point()["sum_assured"]


# ---------------------------------------------------------------------------
# References

disc_rate_ann = ("DataClient", 2160330731208)

model_point_table = ("DataClient", 2160335976392)

mort_table = ("DataClient", 2160317735752)

np = ("Module", "numpy")

pd = ("Module", "pandas")

point_id = 1

premium_table = ("DataClient", 2160336367816)